import sys
import math
from PIL import Image
import numpy
import colorsys

sys.setrecursionlimit(10000)


def draw_image(img_array):
    im = Image.fromarray(img_array)
    im.show()


def mandelbrot_function(z, c, iteration):
    if abs(z) > 2:
        nsmooth = iteration + 1 - math.log(math.log(abs(z)))/math.log(2)
        return iteration #colorsys.hls_to_rgb(0.95 + 10 * nsmooth, 0.6, 1.0)
    if iteration == 1000:
        return iteration#0, 0, 0
    z = z ** 2 + c
    return mandelbrot_function(z, c, iteration + 1)

img_array = []
for j in range(-100, 1):
    row = []
    for i in range(-200, 101):
        row.append(((mandelbrot_function(0, float(i/100.0) + 1j * float(j/100.0), 0))))
    img_array.append(row)
    if j % 100 == 0:
        print str(j/100) + "% finished. "
img_array += list(reversed(img_array[:-1:]))
draw_image(numpy.array(img_array, dtype=numpy.uint8))