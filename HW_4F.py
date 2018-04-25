# -*- coding: utf-8 -*-

"""
Assignment_4F_PIC16
Ashley Wu
ID 204612415
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog
from PyQt5.QtGui import QPainter, QColor 
from PyQt5.QtCore import QTimer

class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        
        self.x = 0
        self.y = 0
        self.mx = 0
        self.my = 0
        self.dx = 0
        self.dy = 0
        self.l = 50
        self.click = False
        self.col = QColor(255,0,0)
        self.resize(600,400)
        self.show()
        
        self.t = QTimer(self)
        self.t.timeout.connect(self.update)
        self.t.start(5)
        
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawEvent(qp)
        qp.end()
        
    def drawEvent(self, qp):
        col = QColor(0,0,0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        
        qp.setBrush(QColor(255,255,255))
        qp.drawRect(0,0,self.width(),self.height())
        
        qp.setBrush(self.col)
        self.x = self.mx - self.dx
        self.y = self.my - self.dy
        qp.drawRect(self.x, self.y, self.l, self.l)       

    def mousePressEvent(self, e):
        if (self.x <= e.x() <= self.x + self.l) and (self.y <= e.y() <= self.y + self.l):
            self.click = True
            self.dx = e.x() - self.x
            self.dy = e.y() - self.y
            self.mx = e.x()
            self.my = e.y()
            
        
    def mouseReleaseEvent(self, e):
        self.click = False
    
    def mouseMoveEvent(self, e):
        if self.click == True:
            self.mx = e.x()
            self.my = e.y()
    
    def mouseDoubleClickEvent(self, e):
        if (self.x <= e.x() <= self.x + self.l) and (self.y <= e.y() <= self.y + self.l):
            self.col = QColorDialog.getColor()
    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    
if __name__ == '__main__':
    main()
    
