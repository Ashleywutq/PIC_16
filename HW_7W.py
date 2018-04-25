# -*- coding: utf-8 -*-

"""
Assignment_7W_PIC16
Ashley Wu
ID 204612415
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack as spft
from scipy.io import wavfile as spwav

rate,y = spwav.read("wooguy4.wav")
y=y[:,0]
t = np.linspace(0,len(y)/float(rate),len(y))

Y = spft.fft(y)
power = abs(Y)
N = len(power)
dt = t[1]-t[0]
fs = spft.fftfreq(N,dt)
plt.plot(fs[0:10000],power[0:10000])
plt.show()

Y[8800:9500]=0
plt.plot(fs[0:10000],Y[0:10000])
plt.show()

out=spft.ifft(Y)
out=out.astype('int16')
spwav.write("HW_7W.wav", rate, out)