import pyqtgraph as pg
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import database
import globals

class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [str(datetime.fromtimestamp(value).hour )+':' + str(datetime.fromtimestamp(value).minute)  for value in values]

class  CustomWidget(pg.GraphicsWindow):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    ptr1 = 0
    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
  
        date_axis = TimeAxisItem(orientation='bottom')
        
        self.list_y2=[]
        self.xli=[]
        self.list_y2=globals.temp_list_value
        self.xli=globals.temp_list_date
        

        self.p1 = self.addPlot(labels =  {'left':'temperature', 'bottom':'Time'},axisItems = {'bottom': date_axis})
        
        last=len(self.xli)-1
        if last >=0:
            self.f=self.xli[last]
            self.p1.setXRange(self.f-60, self.f+60)
            
        self.curve1=self.p1.plot(x=self.xli, y=self.list_y2, pen=(3,3), symbol='o')
        
        #self.curve1=p1.plot(x=[x.timestamp() for x in self.list_x2], y=self.list_y2, pen=(3,3), symbol='o')

        timer = pg.QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(12000) # number of seconds (every 66000) for next update

    def update(self):
        

      
        self.xli=globals.temp_list_date
        self.list_y2=globals.temp_list_value
        
        self.ptr1 += 200
        print(self.xli)
        print(self.list_y2)
        
        
        self.curve1.setData(self.xli,self.list_y2)
        last2=len(self.xli)-1
        if last2 >=0:
            self.f=self.xli[last2]
            self.p1.setXRange(self.f-60, self.f+60)

        #self.p1.setXRange(self.f-200+self.ptr1, self.f+self.ptr1)
      
        

        #self.curve1.setPos(self.ptr1, 0)
        
        

       

    

#if __name__ == '__main__':
    #w = CustomWidget()
    #w.show()
    #QtGui.QApplication.instance().exec_()