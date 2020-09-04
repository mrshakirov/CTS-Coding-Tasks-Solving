from matplotlib import colors as clr
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import sys, os

class Converter:
    def rgb_to_bgr(self, raw_image):
        h, w, c = raw_image.shape
        for x in range(w):
            for y in range(h-1):
                pixel = raw_image[y, x]
                temp = pixel[0]
                pixel[0] = pixel[2]
                pixel[2] = temp

convert = Converter()
img=mpimg.imread(os.path.join(os.path.dirname(sys.argv[0]), 'sample_image.png'))
convert.rgb_to_bgr(img)
plt.imsave("sample_image_updated.png", img)