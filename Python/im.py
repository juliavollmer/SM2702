from __future__ import with_statement
from PIL import Image

##CREATE COLOR DATA BASED ON ALL MICROSCOPE IMAGES

im = Image.open('Averagebinary.jpg') #relative path to file

#load the pixel info
pix = im.load()

#get a tuple of the x and y dimensions of the image
width, height = im.size

arr = []
# #open a file to write the pixel data IN CASE OUTPUT AS EXCEL FILE IS WISHED
# with open('output_file2.csv', 'w+') as f:
#   f.write('R,G,B\n')

  #read the details of each pixel and write them to the file
for x in range(width):
    for y in range(height):
      r = pix[x,y]
      g = pix[x,y]
      b = pix[x,y]
      tu = (r,g,b)
      arr.append(pix[x,y])
    #   if tu != (255,255,255): # remove complete white pixels so only the real microscope image is used, (NOT WITH BINARIZED IMAGES)
    #       arr.append((r,g,b))
    #   else:
    #       pass


    #   f.write('{0},{1},{2}\n'.format(r,g,b))

#arrange the color data new to fit our image
im2 = Image.new("RGB", (600, 749))
pixe = im2.load()
i = 0
for x in range(600):
    for y in range(749):
        pixe[x,y] = arr[i]
        i += 1

# from PIL import ImageEnhance
#
# enh = ImageEnhance.Contrast(im2) ##enhance color contrast if too subtle
# im2 = enh.enhance(1.9).show("30% more contrast")
im2.save("testaverage2.png", "PNG")
