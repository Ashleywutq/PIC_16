# -*- coding: utf-8 -*-

"""
Assignment_3M_PIC16
Ashley Wu
ID 204612415
"""
class Node:
    "This is a Node class"
    
    def __init__ (self, data):
        self.data = data
        self.next = None
        
    def __str__ (self):
        return str(self.data)
        
    def __repr__ (self):
            return repr(self.data)
        
        
class LinkedList:
    "This is a LinkedList class"
    
    def __init__ (self, data):
        first_node = Node(data)
        self.first = first_node
        self.last = first_node
        self.n = 1
        self.next_node = self.first
        
    def append(self, data):
        new_node = Node(data)
        self.last.next = new_node
        self.last = new_node
        self.n = self.n + 1
        
#    def __iter__ (self):
#        return self
#    
#    def next(self):
#        if self.next_node == None :
#            self.next_node = self.first
#            raise StopIteration 
#        return_node = self.next_node
#        self.next_node = self.next_node.next
#        return return_node
   
    def __iter__ (self):
        return self.generator()
    
    def generator (self):
        self.next_node = self.first
        for i in range (self.n):
            return_node = self.next_node
            self.next_node = self.next_node.next
            yield return_node
            
    def __len__ (self):
        return self.n
    
    def __str__ (self):
        string = '['
        for n in self:
            string = string + str(n.data) +"->"
        string = string +']'
        return string
        
    def __repr__ (self):
        string = '['
        for n in self:
            string = string + repr(n.data) +"->"
        string = string +']'
        return string
    
    def __getitem__ (self,index):
        if isinstance (index,int):
            
            if index >= self.n:
                raise IndexError
            n = self.first
            for i in range(index):
                 n = n.next
            return n.data
        
        elif isinstance (index,slice):
         
            start = index.start or 0
            stop = min(index.stop, self.n)
            if stop == None:
                stop = self.n
            step = index.step or 1
            
            if step <= -1:
                raise IndexError
        
            else:
                n = self.first
                for i in range(self.n):
                    if i in range (start, stop, step):
                        if i == start:
                            a = LinkedList(n.data)
                        else:
                            a.append(n.data)
                    n = n.next
                return a
            
        
    def __setitem__ (self,index,data):
        if index >= self.n:
            raise IndexError
        n = self.first
        for i in range(index):
            n = n.next
        n.data = data
        
    def __add__ (self,num):
        a = LinkedList (self[0])
        for i in range(1, self.n):
            a.append (self[i])
        a.append(num)
        return a
    
'''=============testcode============='''

a = LinkedList(0);
a.append(1)
a.append(2)
 
print "40 points if this works"
for n in a:
    print n
 
print ""
 
print "10 points if this works"
for n in a:
    print n
     
print ""
     
print "15 points if both of these work"
for n in a:
    if n.data == 2: # if you wrote your code for n.data == 2, that's OK too
        break
    else:
        print n
  
print ""
        
for n in a:
    if n.data == 2: 
        break
    else:
        print n
 
print ""
 
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)
 
print ""
 
print "5 points each"
print len(a)
print str(a)
print repr(a)
 
print ""
 
print "5 points each. That is, 10 points if the output of the next line is correct"
a[5] = 20
print a[5]
 
print ""
 
print "10 points for correct operation of +"
a+9 # doesn't modify a
print a
 
print ""
 
a = a+9 # appends 9 to a
print a
     
print ""
 
print "10 bonus points if all the following work"
print a[1:5]
print a[1:]
print a[:5]
print a[1::2]
print a[::]
 
print ""
print "-----"
print ""
print "Example output:"
print ""