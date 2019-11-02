# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:31:22 2019

@author: bsodergr

attempting an object oriented version of my spectrogram code

"""
import matplotlib.pyplot as plt #should i import libraries in a class?
import numpy as np
import scipy.io.wavfile as wav
from scipy import signal
from playsound import playsound

class Spectrogram:
    
    fftWidth = 4096
    sampleRate = 44100
   
    def __init__(self, audioInput = 'piano.wav'):
        self.audioInput = audioInput
        self.data = []
        self.f = []
        self.Zxx = []
        #error if not a valid path/file
        #open file explorer also
        #use try/except e.g. except(typeError)
        
        
    def readFile(self):
         self.sampleRate, data = wav.read(self.audioInput)
         data = data[:,0]
         return data
         
    def transform(self):
        data = self.readFile()
        self.f, self.t, self.Zxx = signal.stft(data, self.sampleRate, nperseg = 4096)
        return [self.f, self.t, self.Zxx]
    
    def __str__(self):
        
        log = True
        magnitudegram = np.abs(self.transform()[2])
        f = self.transform()[0]
        t = self.transform()[1]

        if log: magnitudegram = 10*np.log10(magnitudegram)
        
        plt.figure(figsize = (16,10))
        plt.title('Power Spectrogram')
        plt.pcolormesh(t, f, magnitudegram)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()
        
        outputStr = 'Done'
        return outputStr
        
    def play(self):
        playsound(self.audioInput)
        
piano = Spectrogram()
piano.transform()
print(piano)