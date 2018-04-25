# -*- coding: utf-8 -*-

"""
Assignment_4W_PIC16
Ashley Wu
ID 204612415
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, 
                             QMessageBox)
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QCoreApplication, QTimer

class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    
    def initUI(self):
        
        self.setWindowTitle("HW_4W")
        self.setGeometry(200,200,600,400)
        self.x=0
        self.y=0
        self.vx=1
        self.vy=1
        

        self.show()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)
        
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
    
    def drawRectangles(self, qp):
        
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, 2000, 2000)

        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(self.x, self.y, 30, 30)
        
    def animate(self):
        self.checkCollision()
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.update()
        
        
    def checkCollision(self):
        frame = self.frameGeometry() 
        if (self.x+30) > frame.width() or self.x < 0 :
            self.vx = self.vx * (-1)
        if (self.y+50) > frame.height() or self.y < 0:
            self.vy = self.vy * (-1)
            


def main():
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

if __name__ == '__main__':
    main()
    
