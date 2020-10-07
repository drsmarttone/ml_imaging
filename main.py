# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PIL
from PIL import Image
import numpy as np
from PIL.JpegImagePlugin import JpegImageFile
from numpy import ndarray
import matplotlib.pyplot as plt


class Slice:
    def __init__(self, image: JpegImageFile, orientation, level, thickness):
        self.thickness = thickness
        self.orientation = orientation
        aIm = np.array(image)
        if orientation == 'Horz':
            self.aPixels = aIm[level:level + thickness, :]
            slicelength = image.width
        else:
            self.aPixels = aIm[:, level:level + thickness]
            slicelength = image.height

    def getMatch(self,filter : ndarray):
        aPixels.dot(filter)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
