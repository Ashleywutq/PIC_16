# -*- coding: utf-8 -*-

"""
Assignment_2W_PIC16
Ashley Wu
ID 204612415
"""
import time

def my_divide1(a,b):
    return [a[i]/b[i] for i in range(min(len(a),len(b)))]
    


def my_divide2(a,b):
    for i in range(min(len(a),len(b))):
        if b[i]==0:
            print "something is wrong to the input to my_divide2"
            return []
        elif (type (a[i])!= int and type (a[i])!= float):
            print "something is wrong to the input to my_divide2"
            return []
        elif (type (b[i])!= int and type (b[i])!= float):
            print "something is wrong to the input to my_divide2"
            return []
        
    return [a[i]/b[i] for i in range(min(len(a),len(b)))]


def my_divide3(a,b):
    try:
        c=[a[i]/b[i] for i in range(min(len(a),len(b)))]
    except:
        return []
    else:
        return c

def my_divide4(a,b):
    try:
        c=[a[i]/b[i] for i in range(min(len(a),len(b)))]
    except ZeroDivisionError:
        print 'There is a zero in b'
        return []
    except TypeError:
        print 'Non-numeric data detected'
        return []
    else:
        return c
#“There is a zero in b”  “Non-numeric data detected    
    
#begin=time.clock()
#a = range(0,1000000); b = range(1,1000001)
#a = range(0,1000000); b = range(1,1000000)+ [0]
#a = range(0,1000000); b = range(1,1000000)+ ['a']
a=[2]
b=[0]
c = my_divide4(a,b)
print c
#end=time.clock()
#print end-begin