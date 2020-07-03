#Author: Christian Sannemann
#Erstellt am: 03.07.2020
#Zuletzt geändert am: 03.07.2020


import matplotlib.pyplot as plt
import numpy as np
from skimage import io

im = io.imread("scan01.jpeg", as_gray=True)
im = np.uint8(im*255)

hist = np.histogram(im, bins=256)
plt.bar(left=np.arange(256), height=hist[0], align="center",width=0.1)