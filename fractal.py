
import numpy as np
from PIL import Image

HEIGHT = WIDTH = 500

MIN_X = -1.5
MAX_X = 0.5
MIN_Y = -1
MAX_Y = 1

X_INTERVAL = 0.01
Y_INTERVAL = 0.01
MAGNIFICATION = 100
MAX_ITERATIONS = 200 # number of times to compute if number in set
FILE_NAME = "Mandelbrot.png"
# checks if a coordinate is in the mandelbrot set
def inMandelbrot(c, MAX_ITERATIONS): # c is a complex number
    z=0 # initialize start to 0
    for x in range(MAX_ITERATIONS): # number of iterations before determining if c in mandelbrot set
        if z.real + z.imag > 4.0: # if real + imag goes outside circle with radius 2 its not in the set
            return False
        z = z*z + c # iterate the function
    return True # if for loop is complete then c is in the set

def make_mandelbrot(MIN_X, MIN_Y, MAX_X, MAX_Y, MAGNIFICATION, HEIGHT, WIDTH):
  image = Image.new(mode='RGB', size=(WIDTH, HEIGHT))
  for x in (np.arange(MIN_X, MAX_X, X_INTERVAL)):
      for y in np.arange(MIN_Y , MAX_Y, Y_INTERVAL):
          if inMandelbrot(complex(x, y), MAX_ITERATIONS):
              color = (0, 0, 0, 255)
              
          else:
              color = (0, 0, 255, 255)
          image.putpixel((int(x*MAGNIFICATION+WIDTH/2), int(y*MAGNIFICATION+HEIGHT/2)), color )
  return image

if __name__ == "__main__":
  make_mandelbrot(MIN_X, MIN_Y, MAX_X, MAX_Y, MAGNIFICATION, HEIGHT, WIDTH).save(FILE_NAME)
  