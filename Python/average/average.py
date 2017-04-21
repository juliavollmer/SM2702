import os, numpy, PIL
from PIL import Image
from scipy.misc import imsave

## used to make complete black and white images out of the images to observe clear structure, only called when wished
def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

# Access all PNG files in directory
allfiles=os.listdir(os.getcwd())
imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]

# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(imlist[0]).size
N=len(imlist)

# Create a numpy array of floats to store the average (assume RGB images)
arr=numpy.zeros((h,w,3),numpy.float)

# Build up average pixel intensities, casting each image as an array of floats
for im in imlist:
    # binarize_image(im, im, 200) ## binazire images
    imarr=numpy.array(Image.open(im),dtype=numpy.float)
    arr=arr+imarr/N

# Round values in array and cast as 8-bit integer
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

# #alternative method
# images = numpy.array([numpy.array(Image.open(fname)) for fname in imlist])
# arr = numpy.array(numpy.mean(images, axis=(0)), dtype=numpy.uint8)
# out = Image.fromarray(arr)

# Generate, save and preview final image
out=Image.fromarray(arr,mode="RGB")
out.save("Average5.png")
out.show()
