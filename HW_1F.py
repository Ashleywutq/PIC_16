# -*- coding: utf-8 -*-

"""
HW_1F_PIC16
Ashley Wu
ID 204612415
"""
import time

string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\
 tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
 quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\
 consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\
 cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\
 proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
lst = string.split()

dic = { word:lst.count(word) for word in lst}
unique_words = len(dic)
print unique_words
print "count1 is", dic['dolore']

dic_2={}
for word in lst :
    if word not in dic_2:
        dic_2.update({word:1})
    else:
        dic_2[word]=dic_2[word]+1


f = open('HW_1F.txt','r')
string_2 = f.read()
f.close()
lst_2=string_2.split()

##test speed method 1
#begin = time.clock()
#
#dic_3 = { word:lst_2.count(word) for word in lst_2}
#
#end = time.clock()
#print end-begin

#test speed method 2
begin = time.clock()

dic_4={}
for word in lst_2 :
    if word not in dic_4:
        dic_4.update({word:1})
    else:
        dic_4[word]=dic_4[word]+1

end=time.clock()
print end-begin
print "count 2 is", dic_4['found']