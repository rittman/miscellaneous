from PIL import Image

# define the output file
outName = "infographic.png"
w = 1600
h = 800
dims = (w,h) # x and y dimensions of the outfile
out = Image.new("RGB", dims)

# Panel A
ncol=2 # number of columns

# This is the people panel
nman = 12
man = Image.open("man.png")
manw,manh = man.size()

nwoman = 46
woman = Image.open("woman.png")
womanw,womanh = man.size()

# man/woman height
mwh = int(float(w)/((nman+nwoman)/ncol))

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
  left = i%ncol * womanwo
  upper = int(float(i)/ncol * mwh)
  right = left + womanwo
  lower = upper + mwh
  
  out.paste(woman, (left, upper, right, lower))
  
for i in range(nwoman, nwoman+nman):
  left = i%ncol * manwo
  upper = int(float(i)/ncol * mwh)
  right = left + manwo
  lower = upper + mwh
  
  out.paste(man, (left, upper, right, lower))

# text
  
# Panel B
ninfus = 67
# import picture of an injection
inj = Image.open("injection.png")
injw, injh = inh.size

injoh = int(float(h)/ninfus)
injr = injh/injoh
injow = injw*injr

# resize injection picture
inj = inj.resize(injow, injoh)

injleft = right
for i in range(ninfus):
  left = injleft
  upper = i*injoh
  right = left+injow
  lower = upper + injoh

  out.paste(inj, (left, upper, right, lower))

# Panel C


# save file
out.save(outName)

