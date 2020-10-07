import PIL
from PIL import Image
import numpy as np
from PIL.JpegImagePlugin import JpegImageFile
from numpy import ndarray
import matplotlib.pyplot as plt


class Orientation:
    def __init__(self, orient: str):
        if orient in ('H', 'V'):
            self.orientation = orient
        else:
            print('Invalid orientation')


class Filter:
    def __init__(self, width: int, height: int):
        self.filt = np.zeros((width, height))
        self.ht = height
        self.wd = width

    def vertbar(self, starthpos: int, width: int):
        assert starthpos + width <= self.wd
        for h in range(starthpos, starthpos + width):
            for v in range(self.ht):
                self.filt[h, v] = 1

    def vertcentrebar(self, width: int):
        assert width <= self.wd
        starthpos = (self.wd-width)//2
        for h in range(starthpos, starthpos + width):
            for v in range(self.ht):
                self.filt[h, v] = 1

    def horzbar(self, startvpos: int, height: int):
        assert startvpos + height <= self.ht
        for v in range(startvpos, startvpos + height):
            for h in range(self.wd):
                self.filt[h, v] = 1

    def horzcentrebar(self, height: int):
        assert height <= self.ht
        startvpos = (self.ht-height)//2
        for v in range(startvpos, startvpos + height):
            for h in range(self.wd):
                self.filt[h, v] = 1


class Slice:
    def __init__(self, image: JpegImageFile, orientation: Orientation, level, thickness):
        self.thickness = thickness
        self.orientation = orientation
        aim = np.array(image)
        if orientation == 'H':
            self.apixels = aim[level:level + thickness, :]
            slicelength = image.width
        else:
            self.apixels = aim[:, level:level + thickness]
            slicelength = image.height

    def get_match(self, filt: ndarray):
        self.apixels.dot(filt)
