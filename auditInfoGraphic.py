from PIL import Image
from ImageFont import truetype
from ImageDraw import Draw

# define the output file
outName = "infographic.png"
w = 1600
h = 800
dims = (w,h) # x and y dimensions of the outfile
out = Image.new("RGB", dims, color=(254,185,0))    #(239,233,244))

draw = Draw(out)

# set margins and gaps
lmar = 50
umar = 150
bmar = 100
rmar = 50
gap = 150



# Panel A
ncol=8 # number of columns

# This is the people panel
nman = 14
man = Image.open("man.png")
manw,manh = man.size

nwoman = 46
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

# male text
text =  u"\u2640" + " n=" + str(nwoman)
text_w, text_h = font.getsize(text)
draw.text((lmar, umar-text_h), text, fill='white', font=font)

# male text
text =  u"\u2642" + " n=" + str(nman)
draw.text((lmar, h-bmar), text, fill='white', font=font)
  
# Panel B
ncolj1=2
ninfus = 50
colcount = float(ninfus)
colcount += colcount%ncolj1
colcount /= ncolj1

# import picture of an injection
inj = Image.open("injection1.png")
injw, injh = inj.size

injoh = int(float(h-umar-bmar)/colcount)
injr = float(injoh)/injh
injow = int(injw*injr)

# resize injection picture
injo = inj.resize((injow, injoh))

# set where the injections start
injleft = ncol*womanwo + gap
for i in range(ninfus):
  left = i%ncolj1*injow + injleft
  upper = int(float(i)/ncolj1) * injoh + umar
  right = left+injow
  lower = upper + injoh

  out.paste(injo, (left, upper, right, lower), mask=injo)

text = "1st"
text_w, text_h = font.getsize(text)
draw.text((injleft+((ncolj1*injow)/2-(text_w/2)), umar-(text_h)), text, fill='white', font=font)

text = str(ninfus)
text_w, text_h = font.getsize(text)
draw.text((injleft + (ncolj1*injow)/2-(text_w/2), lower+10), text, fill='white', font=font)

# and for follow-up infusions
ncolj2=2
ninfus = 15

# import picture of an injection
inj = Image.open("injection2.png")

# resize injection picture
injo = inj.resize((injow, injoh))

# set where the injections start
injleft2 = ncol*womanwo + gap + ncolj1*injow
for i in range(ninfus):
  left = i%ncolj2*injow + injleft2
  upper = int(float(i)/ncolj2) * injoh + umar
  right = left+injow
  lower = upper + injoh

  out.paste(injo, (left, upper, right, lower), mask=injo)
# Panel C
text = "2nd"

text_w, text_h = font.getsize(text)
draw.text((injleft2 + (ncolj2*injow)/2-(text_w/2), umar-(text_h)), text, fill='white', font=font)

text = str(ninfus)
text_w, text_h = font.getsize(text)
draw.text((injleft2 + (ncolj2*injow)/2-(text_w/2), lower+10), text, fill='white', font=font)

text = "Infusions"
text_w, text_h = font.getsize(text)
draw.text((injleft + (ncolj2*injow + ncolj1*injow)/2-(text_w/2), umar-(text_h*2.2)), text, fill='white', font=font)

# save file
out.save(outName)

