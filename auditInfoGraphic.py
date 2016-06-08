from PIL import Image
from ImageFont import truetype
from ImageDraw import Draw
from string import split
import numpy as np

# set margins and gaps
lmar = 50
umar = 200
bmar = 50
rmar = 50
gap = 150

# set sizes
h = 800
w = 1600

# define colours
green = (63, 104, 28)
yellow = (254,185,0)
cream = (239,233,244)

# import data
f = open("input.txt", "r")
inDict = {x:y for x,y in [v.split() for v in f.readlines()]}

g = open("timeFromSx.csv")
monthList = [int(v.strip('\n')) for v in g.readlines()]


# set output file
outName = "infographic.png"
out = Image.new("RGB", (w,h), color=yellow)
draw = Draw(out)


# Panel A
ncol=8 # number of columns

# This is the people panel
nman = int(inDict["nman"])
man = Image.open("man.png")
manw,manh = man.size

nwoman = int(inDict["nwoman"])
woman = Image.open("woman.png")
womanw,womanh = man.size

# man/woman height
colcount = nman+nwoman
colcount += colcount%ncol
colcount /= ncol

# set individual height
mwh = int(float(h-umar-bmar)/colcount)
print mwh

# calculate man width
manr = float(mwh)/manh
manwo = int(manw*manr)

# calculate woman width
womanr = float(mwh)/womanh
womanwo = int(womanw*womanr)

# resize man/woman for output
mano = man.resize((manwo, mwh))
womano = woman.resize((womanwo, mwh))

# paste women
count = 0

for i in range(nwoman):
  left = i%ncol * womanwo + lmar
  upper = int(float(i)/ncol) * mwh + umar
  right = left + womanwo
  lower = upper + mwh
  out.paste(womano, (left, upper, right, lower), mask=womano)
  
for i in range(nwoman, nwoman+nman):
  left = i%ncol * manwo + lmar
  upper = int(float(i)/ncol) * mwh + umar
  right = left + manwo
  lower = upper + mwh
  
  out.paste(mano, (left, upper, right, lower), mask=mano)

# text
font_size=14
font = truetype('/usr/share/fonts/truetype/msttcorefonts/arialbd.ttf',
                        int(300 * font_size / 72.0))
                        
smallFont_size = 11 
smallFont = truetype('/usr/share/fonts/truetype/msttcorefonts/arialbd.ttf',
                        int(300 * smallFont_size / 72.0))
                        
bigFont_size = 18 
bigFont = truetype('/usr/share/fonts/truetype/msttcorefonts/arialbd.ttf',
                        int(300 * bigFont_size / 72.0))

                        
# female text
text =  str(nwoman) + u"\u2640" + "   " + str(nman) + u"\u2642"
text_w, text_h = font.getsize(text)
draw.text((lmar, umar-text_h), text, fill=cream, font=font)

## male text
#text =  
#draw.text((lmar, h-bmar), text, fill=cream, font=font)
  
# Panel B
ncolj1=2
ninfus = int(inDict["ninfus1"])
colcount = float(ninfus)
colcount += colcount%ncolj1
colcount /= ncolj1

# import picture of an injection
inj = Image.open("injection1.png")
injw, injh = inj.size

textGap = 75 # gap under the injections for x text
injoh = int(float(h-umar-bmar-textGap+50)/colcount)
injr = float(injoh)/injh
injow = int(injw*injr)

# resize injection picture
injo1 = inj.resize((injow, injoh))

# set where the injections start
injleft = ncol*womanwo + gap
for i in range(ninfus):
  left = i%ncolj1*injow + injleft
  lower = h-bmar-textGap - int(float(i)/ncolj1) * injoh
  right = left+injow
  upper = lower - injoh

  out.paste(injo1, (left, upper, right, lower), mask=injo1)

text = "1st"
text_w, text_h = smallFont.getsize(text)
draw.text((injleft+((ncolj1*injow)/2-(text_w/2)), h-bmar-textGap), text, fill=cream, font=smallFont)

text = str(ninfus)
text_w, text_h = smallFont.getsize(text)
if i%2!=1:
    upper -= injoh
draw.text((injleft + (ncolj1*injow)/2-(text_w/2), upper-text_h), text, fill=cream, font=smallFont)

# and for follow-up infusions
ncolj2=2
ninfus = int(inDict["ninfus2"])

# import picture of an injection
inj = Image.open("injection2.png")

# resize injection picture
injo2 = inj.resize((injow, injoh))

# set where the injections start
injleft2 = ncol*womanwo + gap + ncolj1*injow
for i in range(ninfus):
  left = i%ncolj2*injow + injleft2
  lower = h-bmar-textGap - int(float(i)/ncolj2) * injoh
  right = left+injow
  upper  = lower - injoh

  out.paste(injo2, (left, upper, right, lower), mask=injo2)

text = "2nd"
text_w, text_h = smallFont.getsize(text)
draw.text((injleft2 + (ncolj2*injow)/2-(text_w/2),  h-bmar-textGap), text, fill=cream, font=smallFont)

text = str(ninfus)
text_w, text_h = smallFont.getsize(text)
if i%2!=1:
    upper -= injoh
draw.text((injleft2 + (ncolj2*injow)/2-(text_w/2), upper-text_h), text, fill=cream, font=smallFont)


text = "infusion"
text_w, text_h = font.getsize(text)
ypos = h-bmar-text_h
draw.text((injleft + (ncolj2*injow + ncolj1*injow)/2-(text_w/2), h-bmar-text_h+20), text, fill=cream, font=font)

# Age
circle = Image.open("circle.png")
cw,ch = circle.size
left = w/2+75
upper = umar

cdraw = Draw(circle)

text = "Age"
text_w, text_h = smallFont.getsize(text)
cdraw.text((cw/2 - text_w/2, ch/4), text, fill=cream, font=smallFont)
text = inDict["meanAge"]
text_w, text_h = font.getsize(text)
cdraw.text((cw/2 - text_w/2, ch*0.45), text, fill=cream, font=font)

out.paste(circle, (left, upper), mask=circle)

# EDSS
circle = Image.open("circle.png")
cw,ch = circle.size
left = w/2
upper = umar

cdraw = Draw(circle)

text = "EDSS"
text_w, text_h = smallFont.getsize(text)
cdraw.text((cw/2 - text_w/2, ch/4), text, fill=cream, font=smallFont)
text = inDict["medianEDSS"]
text_w, text_h = font.getsize(text)
cdraw.text((cw/2 - text_w/2, ch*0.45), text, fill=cream, font=font)
left = int(w*0.75)
upper = umar
out.paste(circle, (left, upper), mask=circle)


# time from symptom onset
sxLeft = 875
sxRight = w-rmar - 40
sxBottom = h-bmar - 75
sxLength = sxRight-sxLeft
sxMin = np.min(monthList)
sxMax = np.max(monthList)
monthList.remove(sxMin)
monthList.remove(sxMax)
sxMinX = (sxLength/sxMax) * sxMin
sxWidth = 75

# end injection
injo1 = injo1.rotate(90, expand=True)
injow, injoh = injo1.size
out.paste(injo1, (sxRight-(injow/2), sxBottom-injoh-sxWidth/2), mask=injo1)

# start injection
out.paste(injo1, (sxLeft + sxMinX - (injow/2), sxBottom-injoh-sxWidth/2), mask=injo1)


# length of time since diagnosis/symptoms
draw.line((sxLeft,sxBottom, sxRight, sxBottom), fill=green, width=sxWidth)

text = "0"
text_w, text_h = smallFont.getsize(text)
draw.text((sxLeft - text_w/2, sxBottom+sxWidth/2), text, fill=cream, font=smallFont)

text = str(sxMax)
text_w, text_h = smallFont.getsize(text)
draw.text((sxRight - text_w/2, sxBottom+sxWidth/2), text, fill=cream, font=smallFont)

text = "Months from symptom onset"
text_w, text_h = smallFont.getsize(text)
draw.text((sxLeft, sxBottom-text_h/2), text, fill=yellow, font=smallFont)

smallInjoh = injoh/2
smallInjow = injow/2

injo1 = injo1.resize((smallInjow, smallInjoh))
for i in monthList:
    out.paste(injo1, (sxLeft + (sxLength/sxMax)*i, sxBottom-smallInjoh-sxWidth/2), mask=injo1)


# title
text = "Alemtuzumab patients"
text_w, text_h = bigFont.getsize(text)
draw.text((5,5), text, fill=cream, font=bigFont)

# save file
out.save(outName)

