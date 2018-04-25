# -*- coding: utf-8 -*-

"""
Assignment_8M_PIC16
Ashley Wu
ID 204612415
"""


from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

#perfect guess z0
guessx=np.linspace(0,1,50)
guessy=np.sqrt(1-guessx**2)
z0=np.zeros(50)
z0[0]=guessx[49]
z0[1:50]=guessy[0:49]

#takes z and return x and y
def z2xy(z):
    x=np.linspace(0,z[0],50)
    y=np.zeros(50)
    y[0:49]=z[1:50]
    y[49]=0
    return x,y

#return negative of area
def obj(z):
    x,y=z2xy(z)
    area=np.trapz(y,x)
    return -area

#define constraint 
p=np.pi/2
def con(z):
    x,y=z2xy(z)
    dx=x[1]-x[0]
    dy=np.zeros(49)
    dy[:]=y[1:50]-y[0:49]
    larray=np.sqrt(dy**2+dx**2)
    l=np.sum(larray)
    return l-p

#bound
bnd=[(0,p)for i in range(0,50)]


#specify con
condict={"type":'eq',"fun":con}
#print minimize(obj,z0,bounds=bnd,constraints=condict)

#random z0
z0=np.random.rand(50)*p
x0,y0=z2xy(z0)
z=minimize(obj,z0,bounds=bnd,constraints=condict).x
x,y=z2xy(z)



plt.plot(x,y,x0,y0)
plt.legend(["solution","guess"])
plt.axis('equal')
plt.show()

    