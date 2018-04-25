# -*- coding: utf-8 -*-

"""
Assignment_8M_PIC16
Ashley Wu
ID 204612415
"""

from scipy.misc import imread # using scipy's imread
import cv2
import numpy as np
from sklearn import svm

def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # real letters will be bigger than 10px by 10px
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
    pure_white = 255.
    white = np.max(img)
    black = np.min(img)
    thresh = (white+black)/2.0
    binarized = img<thresh
    row_bounds = boundaries(binarized, axis = 0) 
    cropped = []
    for r1,r2 in row_bounds:
        img = binarized[r1:r2,:]
        col_bounds = boundaries(img,axis=1)
        rects = [r1,r2,col_bounds[0][0],col_bounds[0][1]]
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/pure_white))
    return cropped

## Example usage
#big_img = imread("a.png", flatten = True) # flatten = True converts to grayscale
#cv2.imshow("a",big_img/255)
#cv2.waitKey(1000)
#cv2.destroyAllWindows()
#
#imgs = separate(big_img) # separates big_img (pure white = 255) into array of little images (pure white = 1.0)
#for img in imgs:
#    cv2.imshow("a",img) 
#    cv2.waitKey(250)
#cv2.destroyAllWindows()


big_img_a = imread("a.jpeg", flatten = True)
big_img_b = imread("b.jpeg", flatten = True)
big_img_c = imread("c.jpeg", flatten = True)

imgs_a = separate(big_img_a)
imgs_b = separate(big_img_b)
imgs_c = separate(big_img_c) # separates big_img (pure white = 255) into array of little images (pure white = 1.0)
imgs=imgs_a+imgs_b+imgs_c
data=np.ones(((len(imgs)),25))

i=0
for img in imgs:
    img2=img[0:img.shape[0]-img.shape[0]%5:img.shape[0]/5,0:img.shape[1]-img.shape[1]%5:img.shape[1]/5]
    flatimg2=img2.reshape((25))
    data[i,:]=flatimg2
    i=i+1

target_a=np.full((len(imgs_a)),0)
target_b=np.full((len(imgs_b)),1)
target_c=np.full((len(imgs_c)),2)
target=np.append(target_a,target_b)
target=np.append(target,target_c)

#all random partition, accuracy will change 
def partition(data,target,p):
    train_i=np.random.choice(target.shape[0],int(target.shape[0]*p),False)
    all_i=np.arange(target.shape[0])
    all_i[train_i]=-1
    test_i=all_i[all_i>-1]
    
    train_data=data[train_i,:]
    train_target=target[train_i]
    test_data=data[test_i,:]
    test_target=target[test_i]
    return train_data, train_target, test_data, test_target

#only order change, n is number of trials, accuracy won't change 
def partition1(data,target,n):
    train_i=np.arange(30)[0:30-30%n:30/n]
    train_i = np.random.permutation(train_i)
    all_i=np.arange(target.shape[0])
    all_i[train_i]=-1
    test_i=all_i[all_i>-1]
    
    train_data=data[train_i,:]
    train_target=target[train_i]
    test_data=data[test_i,:]
    test_target=target[test_i]
    return train_data, train_target, test_data, test_target

#train data 
train_data, train_target, test_data, test_target=partition(data,target,.5)
#linear clf
clf=svm.LinearSVC()
#clf = svm.SVC(gamma = 0.0001, C= 100, kernel="poly")
clf.fit(train_data,train_target)
predict=clf.predict(test_data)
print "Predicted: ", predict
print "Truth", test_target   
accuracy = sum(predict==test_target)*1.0/(predict.shape[0])
print "Accuracy: ", accuracy*100, "%"