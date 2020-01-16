from PIL import Image
import numpy as np
import sys
import argparse

CLI = argparse.ArgumentParser()

CLI.add_argument(
        "--targetColor",
        nargs="*",
        type=int,
        default=(255, 0, 0, 255)
)

CLI.add_argument(                                                                                                                                                                                                          "--destinationColor",
        nargs="*",                                                                                                                                                                                                         type=int,
        default=(0, 0, 0, 255)
)

CLI.add_argument(
        "--imagePath",
        nargs="*",
        type=str,
        default="image.png"
)

args = CLI.parse_args()

#Get target und destination color
targetColor = args.targetColor
destinationColor = args.destinationColor

print(args.targetColor)

#Get image path
imagePath = args.imagePath

#Load mage and extracting data
imageA = Image.open(imagePath)
imageAPixels = imageA.load()
width, height = imageA.size

#Prepare array[height, width] => RGBA
data = np.asarray(imageA, dtype='uint8')
newData = np.zeros((height, width, 4))

#Iterate through imagedata
for x in range(width):
    for y in range(height):
        currentPixel = data[y, x]
        if (data[y, x] == targetColor).all():
            currentPixel= destinationColor
        newData[y, x] = currentPixel

#save new image
newImg = Image.fromarray(newData.astype('uint8'), 'RGBA')
newImg.save("processedImage.png")
