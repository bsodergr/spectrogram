# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:37:46 2019

@author: bsodergr

quick wav visualizer
"""

import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

file1 = 'piano.wav'
file2 = 'transformed.wav'

rate1, data1 = wav.read(file1)
rate2, data2 = wav.read(file2)

x = np.arange(len(data1))

plt.plot(data1)
plt.title('piano')
plt.show()

plt.plot(data2)
plt.title('transformed')
plt.show()