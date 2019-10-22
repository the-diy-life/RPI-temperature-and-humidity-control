# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Temperature.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow #this is to enable the self.sender function

import globals

from PyQt5.QtCore import QTimer
from datetime import datetime
import database
import Adafruit_DHT
import time
from plotter_temp import CustomWidget

class Ui_Temperature(QMainWindow):
    def setupUi(self, Temperature):
        Temperature.setObjectName("Temperature")
        Temperature.resize(800, 480)
        Temperature.setMinimumSize(QtCore.QSize(800, 480))
        Temperature.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Temperature)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ControlFrame = QtWidgets.QFrame(Temperature)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlFrame.sizePolicy().hasHeightForWidth())
        self.ControlFrame.setSizePolicy(sizePolicy)
        self.ControlFrame.setMinimumSize(QtCore.QSize(466, 420))
        self.ControlFrame.setObjectName("ControlFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ControlFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = CustomWidget(self.ControlFrame)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.lblCurrentReading = QtWidgets.QLabel(self.ControlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCurrentReading.sizePolicy().hasHeightForWidth())
        self.lblCurrentReading.setSizePolicy(sizePolicy)
        self.lblCurrentReading.setStyleSheet("color:\'black\'")
        self.lblCurrentReading.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentReading.setObjectName("lblCurrentReading")
        self.verticalLayout.addWidget(self.lblCurrentReading)
        self.verticalLayout_5.addWidget(self.ControlFrame)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.RightMenusFrame = QtWidgets.QFrame(Temperature)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightMenusFrame.sizePolicy().hasHeightForWidth())
        self.RightMenusFrame.setSizePolicy(sizePolicy)
        self.RightMenusFrame.setMinimumSize(QtCore.QSize(0, 460))
        self.RightMenusFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.RightMenusFrame.setSizeIncrement(QtCore.QSize(0, 0))
        self.RightMenusFrame.setObjectName("RightMenusFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.RightMenusFrame)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.MenusSpacingFrame = QtWidgets.QFrame(self.RightMenusFrame)
        self.MenusSpacingFrame.setMinimumSize(QtCore.QSize(200, 200))
        self.MenusSpacingFrame.setObjectName("MenusSpacingFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.MenusSpacingFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.MenusFrame = QtWidgets.QFrame(self.MenusSpacingFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenusFrame.sizePolicy().hasHeightForWidth())
        self.MenusFrame.setSizePolicy(sizePolicy)
        self.MenusFrame.setMinimumSize(QtCore.QSize(121, 200))
        self.MenusFrame.setObjectName("MenusFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MenusFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnHome = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy)
        self.btnHome.setMinimumSize(QtCore.QSize(0, 0))
        self.btnHome.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnHome.setObjectName("btnHome")
        self.verticalLayout_2.addWidget(self.btnHome)
        self.btnControlCenter = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnControlCenter.sizePolicy().hasHeightForWidth())
        self.btnControlCenter.setSizePolicy(sizePolicy)
        self.btnControlCenter.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnControlCenter.setObjectName("btnControlCenter")
        self.verticalLayout_2.addWidget(self.btnControlCenter)
        self.btnManualControl = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnManualControl.sizePolicy().hasHeightForWidth())
        self.btnManualControl.setSizePolicy(sizePolicy)
        self.btnManualControl.setMinimumSize(QtCore.QSize(0, 0))
        self.btnManualControl.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnManualControl.setObjectName("btnManualControl")
        self.verticalLayout_2.addWidget(self.btnManualControl)
        self.btnHumidity = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHumidity.sizePolicy().hasHeightForWidth())
        self.btnHumidity.setSizePolicy(sizePolicy)
        self.btnHumidity.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnHumidity.setObjectName("btnHumidity")
        self.verticalLayout_2.addWidget(self.btnHumidity)
        self.horizontalLayout_5.addWidget(self.MenusFrame)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.MenusSpacingFrame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem3)
        self.StatusFrame = QtWidgets.QFrame(self.RightMenusFrame)
        self.StatusFrame.setMinimumSize(QtCore.QSize(202, 231))
        self.StatusFrame.setObjectName("StatusFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.StatusFrame)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.lblTime = QtWidgets.QLabel(self.StatusFrame)
        self.lblTime.setMinimumSize(QtCore.QSize(200, 21))
        self.lblTime.setMaximumSize(QtCore.QSize(16777215, 21))
        self.lblTime.setStyleSheet("qproperty-alignment:AlignCenter;\n"
"background-color:White;\n"
"color:blue;\n"
"font-size:12px;\n"
"font-weight:bold;")
        self.lblTime.setObjectName("lblTime")
        self.verticalLayout_3.addWidget(self.lblTime)
        self.verticalLayout_4.addWidget(self.StatusFrame)
        self.gridLayout.addWidget(self.RightMenusFrame, 0, 2, 2, 1)
        self.lblTemperature = QtWidgets.QLabel(Temperature)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemperature.setFont(font)
        self.lblTemperature.setObjectName("lblTemperature")
        self.gridLayout.addWidget(self.lblTemperature, 0, 0, 1, 2)

        self.retranslateUi(Temperature)
        QtCore.QMetaObject.connectSlotsByName(Temperature)

    def retranslateUi(self, Temperature):
        _translate = QtCore.QCoreApplication.translate
        Temperature.setWindowTitle(_translate("Temperature", "Form"))
        self.lblCurrentReading.setText(_translate("Temperature", "Temperature:  30C"))
        self.btnHome.setText(_translate("Temperature", "Home"))
        self.btnControlCenter.setText(_translate("Temperature", "Control\n"
"Center"))
        self.btnManualControl.setText(_translate("Temperature", "Manual\n"
"Control"))
        self.btnHumidity.setText(_translate("Temperature", "Humidity"))
        self.lblTime.setText(_translate("Temperature", "10-10-2019 17:06:21"))
        self.lblTemperature.setText(_translate("Temperature", "Temperature State"))
        ##################################################
        ##################################################
        self.updateTime()
        self.startTimeUpdateTimer()

        self.update_read()
        self.startTimeUpdateRead()

        self.btnHome.clicked.connect(self.open_home_screen)
        self.btnManualControl.clicked.connect(self.open_manuel_control)
        self.btnHumidity.clicked.connect(self.open_humidity_screen)
        self.btnControlCenter.clicked.connect(self.open_control_screen)

    def open_home_screen(self):
        globals.temp.hide()
        globals.Home.show()
    
    def open_humidity_screen(self):
        globals.temp.hide()
        globals.humidity.show()

    def open_control_screen(self):
        globals.temp.hide()
        globals.control.show()

    def open_manuel_control(self):
        globals.temp.hide()
        globals.manuel.show()

    def updateTime(self):
            now = datetime.now()
            # H:M:S - DD/MM/YY
            dt_string = now.strftime("%H:%M:%S %d-%b-%Y")
            self.lblTime.setText(dt_string)

    def startTimeUpdateTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000) 

    def startTimeUpdateRead(self):
        self.timer_read = QTimer()
        self.timer_read.timeout.connect(self.update_read)
        self.timer_read.start(9000) 


    def update_read(self):
       
        
            temp= "current temperature: {0:0.1f}C".format(globals.temperature_read)
            #print(temp)
            self.lblCurrentReading.setText(temp)
            #print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
       
        
   
 
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Temperature = QtWidgets.QWidget()
    ui = Ui_Temperature()
    ui.setupUi(Temperature)
    Temperature.show()
    sys.exit(app.exec_())
