from PIL import Image
import numpy as np

#Load mage and extracting data
imageA = Image.open("image.png")
imageAPixels = imageA.load()
width, height = imageA.size

#Prepare array[height, width] => RGBA
data = np.asarray(imageA, dtype='uint8')
newData = np.zeros((height, width, 4))

#Iterate through imagedata
for x in range(width):
    for y in range(height):
        currentPixel = data[y, x]
        if (data[y, x] == (237, 27, 36, 255)).all():
            currentPixel= [78, 95, 191, 255]
        newData[y, x] = currentPixel

#save new image
newImg = Image.fromarray(newData.astype('uint8'), 'RGBA')
newImg.save('newImg.png')
