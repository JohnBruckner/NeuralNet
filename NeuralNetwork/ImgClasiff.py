#!usr/bin/python3

import statistics
import sys
import time
import subprocess
import PIL
import scipy
#import theano
import numpy as np
import matplotlib.pyplot as plt


def toMatrix(img):
    try:
        imgMatrix = np.asmatrix(img) # fails in certain cases

    except:
        imgMatrix = np.asarray(img)

    return imgMatrix


def grayScale(imgArr):
    balanceArr = []
    newArr = imgArr
    shades = 20
    convFact = 255/(shades-1)
    #alphaCh = len
    for eRow in imgArr:
        for ePix in eRow:
            avgNum = statistics.mean(ePix[:2])
            balanceArr.append(avgNum)

    balance = statistics.mean(balanceArr)
    for eRow in newArr:
        for ePix in eRow:
            '''if statistics.mean(ePix[:3]) > balance:
                ePix[0] = 255
                ePix[1] = 255
                ePix[2] = 255
                ePix[3] = 255
            else:
                ePix[0] = 0
                ePix[1] = 0
                ePix[2] = 0
                ePix[3] = 255'''

            avg = (ePix[0] + ePix[1] + ePix[2]) / 3 # (ePix[0]*0.3 + ePix[1]*0.59 + ePix[2]*0.11)
            gray = int((avg / convFact) + 0.5) * convFact
            ePix[0] = gray
            ePix[1] = gray
            ePix[2] = gray

    return newArr

imgPath = sys.argv[0]
rawImage = PIL.Image.open(imgPath)
matrix = toMatrix(rawImage)
