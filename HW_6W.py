# -*- coding: utf-8 -*-

"""
Assignment_6W_PIC16
Ashley Wu
ID 204612415
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 

#read in imga as an array
imga=mpimg.imread('a.jpg')
print "a shape", imga.shape

imgb=mpimg.imread('b.jpg')
print 'b shape', imgb.shape

#a+b=c
imgc=imga.copy()
imgc[250:650,100:500,:]=imgb
print 'c shape', imgc.shape
plt.imshow(imgc)
plt.show()
mpimg.imsave('c.jpg',imgc)

#g h difference 
imgg=mpimg.imread('g.jpg')
imgg=imgg.astype(float)
print 'g shape', imgg.shape,imgg.dtype

imgh=mpimg.imread('h.jpg')
imgh=imgh.astype(float)
print 'h shape', imgh.shape, imgh.dtype

imgi=np.absolute(imgg-imgh)
imgi=imgi.astype(np.uint8)
plt.imshow(imgi)
plt.show()
mpimg.imsave('i.jpg',imgi)

#e change background
imgd=mpimg.imread('d.jpg')
print "d shape", imgd.shape

imge=mpimg.imread('e.jpg')
print "e shape", imge.shape
imge.setflags(write=1)
imge[np.logical_and(imge[:,:,1]>200,imge[:,:,2]<40,imge[:,:,0]<40)]=0
plt.imshow(imge)
plt.show()

imgf=imgd.copy()
for i in range(161):
    for j in range(165):
        if imge[i,j,1]!=0:
            imgf[540+i,250+j,:]=imge[i,j,:]
plt.imshow(imgf)
plt.show()
mpimg.imsave('f.jpg',imgf)
