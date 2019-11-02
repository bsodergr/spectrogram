import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
from scipy import signal
from playsound import playsound

fftWidth = 4096

def specgramize(audioFile = 'piano.wav', log = True, 
                  display = True, play = False):
    
    sampleRate, data = wav.read(audioFile)
    data = data[:,0]

    
    #time = len(data[:,0])/sampleRate
    #print('length of the audio is ', time,' seconds')
    
    f, t, Zxx = signal.stft(data, sampleRate, nperseg = 4096)
    
    magnitudegram = np.abs(Zxx)
    phasegram = np.angle(Zxx)
    
    if log: magnitudegram = 10*np.log10(magnitudegram)
    
    if display:
        plt.figure(figsize = (16,10))
        plt.title('Power Spectrogram')
        plt.pcolormesh(t, f, magnitudegram)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()
        
#        plt.figure(figsize = (16,1))
#        plt.title('Phasegram')
#        plt.pcolormesh(t, f, phasegram)
#        plt.ylabel('Phase [rad?]')
#        plt.xlabel('Time [sec]')
#        plt.show()
        
    if play: playsound(audioFile)
    
    return Zxx
    

def despecgramize(Zxx, log = False, play = False):
    t, xformedAudio = signal.istft(Zxx, fs = sampleRate, 
                                            nperseg = fftWidth)
    xformedAudio /= (np.max(np.abs(xformedAudio)))
    wav.write('transformed.wav', sampleRate, xformedAudio)
    print('wrote wav file')
    
    if play: playsound('transformed.wav')
    
    return xformedAudio


spec = specgramize()
audio = despecgramize(spec)
