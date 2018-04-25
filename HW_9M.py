#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
author: Ashley Wu
PIC_16 HW9M
204612415
"""

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

def f(y,t):
    m=1
    l=1
    g=1
    x=y[0]
    dx=y[1]
    dy=np.zeros(y.shape)
    dy[0]=dx
    dy[1]=-g/l*np.sin(x)
    return dy
    
t = np.linspace(0,10,100)
f0=(1,0)
y, info = spint.odeint(f,f0,t,full_output=True)

plt.plot(t,y[:,0])
plt.show()