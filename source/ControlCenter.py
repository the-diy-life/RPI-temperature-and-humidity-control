# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlCenter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import  QMessageBox

from PyQt5.QtWidgets import QMainWindow #this is to enable the self.sender function

import globals
from number_pad import numberPopup
from PyQt5.QtCore import QTimer
from datetime import datetime
import database
from relay_lib_seeed import *

class Ui_Control(QMainWindow):
    def setupUi(self, Control):
        Control.setObjectName("Control")
        Control.resize(800, 480)
        Control.setMinimumSize(QtCore.QSize(800, 480))
        self.gridLayout = QtWidgets.QGridLayout(Control)
        self.gridLayout.setObjectName("gridLayout")
        self.RelayNoEnableFrame = QtWidgets.QFrame(Control)
        self.RelayNoEnableFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.RelayNoEnableFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.RelayNoEnableFrame.setObjectName("RelayNoEnableFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.RelayNoEnableFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.RelayNoSpaceFrame = QtWidgets.QFrame(self.RelayNoEnableFrame)
        self.RelayNoSpaceFrame.setObjectName("RelayNoSpaceFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.RelayNoSpaceFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.RelayNoFrame = QtWidgets.QFrame(self.RelayNoSpaceFrame)
        self.RelayNoFrame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.RelayNoFrame.setObjectName("RelayNoFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.RelayNoFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblRelay = QtWidgets.QLabel(self.RelayNoFrame)
        self.lblRelay.setMinimumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblRelay.setFont(font)
        self.lblRelay.setObjectName("lblRelay")
        self.horizontalLayout_3.addWidget(self.lblRelay)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnRelayNumber = QtWidgets.QPushButton(self.RelayNoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRelayNumber.sizePolicy().hasHeightForWidth())
        self.btnRelayNumber.setSizePolicy(sizePolicy)
        self.btnRelayNumber.setMinimumSize(QtCore.QSize(101, 51))
        self.btnRelayNumber.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnRelayNumber.setObjectName("btnRelayNumber")
        self.horizontalLayout_3.addWidget(self.btnRelayNumber)
        self.verticalLayout_6.addWidget(self.RelayNoFrame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_6.addWidget(self.RelayNoSpaceFrame)
        spacerItem3 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.EnableFrame = QtWidgets.QFrame(self.RelayNoEnableFrame)
        self.EnableFrame.setMinimumSize(QtCore.QSize(133, 92))
        self.EnableFrame.setObjectName("EnableFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.EnableFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem4)
        self.btnENDISABLE = QtWidgets.QPushButton(self.EnableFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnENDISABLE.sizePolicy().hasHeightForWidth())
        self.btnENDISABLE.setSizePolicy(sizePolicy)
        self.btnENDISABLE.setMinimumSize(QtCore.QSize(121, 71))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btnENDISABLE.setFont(font)
        self.btnENDISABLE.setStyleSheet("background-color:\'red\';\n"
"color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnENDISABLE.setObjectName("btnENDISABLE")
        self.verticalLayout_5.addWidget(self.btnENDISABLE)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_6.addWidget(self.EnableFrame)
        self.gridLayout.addWidget(self.RelayNoEnableFrame, 0, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.RightMenusFrame = QtWidgets.QFrame(Control)
        self.RightMenusFrame.setMinimumSize(QtCore.QSize(0, 460))
        self.RightMenusFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.RightMenusFrame.setObjectName("RightMenusFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.RightMenusFrame)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.MenusSpacingFrame = QtWidgets.QFrame(self.RightMenusFrame)
        self.MenusSpacingFrame.setMinimumSize(QtCore.QSize(200, 200))
        self.MenusSpacingFrame.setObjectName("MenusSpacingFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.MenusSpacingFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.MenusFrame = QtWidgets.QFrame(self.MenusSpacingFrame)
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
        self.btnTemperature = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTemperature.sizePolicy().hasHeightForWidth())
        self.btnTemperature.setSizePolicy(sizePolicy)
        self.btnTemperature.setMinimumSize(QtCore.QSize(0, 0))
        self.btnTemperature.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnTemperature.setObjectName("btnTemperature")
        self.verticalLayout_2.addWidget(self.btnTemperature)
        self.btnHumidity = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHumidity.sizePolicy().hasHeightForWidth())
        self.btnHumidity.setSizePolicy(sizePolicy)
        self.btnHumidity.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnHumidity.setObjectName("btnHumidity")
        self.verticalLayout_2.addWidget(self.btnHumidity)
        self.btnManualControl = QtWidgets.QPushButton(self.MenusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnManualControl.sizePolicy().hasHeightForWidth())
        self.btnManualControl.setSizePolicy(sizePolicy)
        self.btnManualControl.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnManualControl.setObjectName("btnManualControl")
        self.verticalLayout_2.addWidget(self.btnManualControl)
        self.horizontalLayout_5.addWidget(self.MenusFrame)
        spacerItem8 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.MenusSpacingFrame)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem9)
        self.StatusFrame = QtWidgets.QFrame(self.RightMenusFrame)
        self.StatusFrame.setMinimumSize(QtCore.QSize(202, 231))
        self.StatusFrame.setObjectName("StatusFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.StatusFrame)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.StatusFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblONIcon = QtWidgets.QLabel(self.frame)
        self.lblONIcon.setMinimumSize(QtCore.QSize(129, 129))
        self.lblONIcon.setMaximumSize(QtCore.QSize(129, 129))
        self.lblONIcon.setText("")
        self.lblONIcon.setPixmap(QtGui.QPixmap("/home/pi/dht/ONresized.png"))
        self.lblONIcon.setObjectName("lblONIcon")
        self.horizontalLayout_4.addWidget(self.lblONIcon)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem10)
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
        self.gridLayout.addWidget(self.RightMenusFrame, 0, 4, 4, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem11, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 2, 0, 1, 1)
        self.ControlFrame = QtWidgets.QFrame(Control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlFrame.sizePolicy().hasHeightForWidth())
        self.ControlFrame.setSizePolicy(sizePolicy)
        self.ControlFrame.setObjectName("ControlFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ControlFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TypeFrame = QtWidgets.QFrame(self.ControlFrame)
        self.TypeFrame.setObjectName("TypeFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TypeFrame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblType = QtWidgets.QLabel(self.TypeFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblType.setFont(font)
        self.lblType.setObjectName("lblType")
        self.horizontalLayout.addWidget(self.lblType)
        self.cbxType = QtWidgets.QComboBox(self.TypeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbxType.sizePolicy().hasHeightForWidth())
        self.cbxType.setSizePolicy(sizePolicy)
        self.cbxType.setMinimumSize(QtCore.QSize(200, 50))
        self.cbxType.setStyleSheet("background-color:\'grey\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.cbxType.setObjectName("cbxType")
        self.cbxType.addItem("")
        self.cbxType.addItem("")
        self.horizontalLayout.addWidget(self.cbxType)
        self.verticalLayout.addWidget(self.TypeFrame)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem13)
        self.SetPointFrame = QtWidgets.QFrame(self.ControlFrame)
        self.SetPointFrame.setObjectName("SetPointFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SetPointFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblOnSetPoint = QtWidgets.QLabel(self.SetPointFrame)
        self.lblOnSetPoint.setMinimumSize(QtCore.QSize(164, 69))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblOnSetPoint.setFont(font)
        self.lblOnSetPoint.setObjectName("lblOnSetPoint")
        self.horizontalLayout_2.addWidget(self.lblOnSetPoint)
        self.btnONSetPoint = QtWidgets.QPushButton(self.SetPointFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnONSetPoint.sizePolicy().hasHeightForWidth())
        self.btnONSetPoint.setSizePolicy(sizePolicy)
        self.btnONSetPoint.setMinimumSize(QtCore.QSize(110, 85))
        self.btnONSetPoint.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnONSetPoint.setObjectName("btnONSetPoint")
        self.horizontalLayout_2.addWidget(self.btnONSetPoint)
        self.verticalLayout.addWidget(self.SetPointFrame)
        self.SetPointFrame_2 = QtWidgets.QFrame(self.ControlFrame)
        self.SetPointFrame_2.setObjectName("SetPointFrame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.SetPointFrame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblOFFSetPoint = QtWidgets.QLabel(self.SetPointFrame_2)
        self.lblOFFSetPoint.setMinimumSize(QtCore.QSize(164, 69))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblOFFSetPoint.setFont(font)
        self.lblOFFSetPoint.setObjectName("lblOFFSetPoint")
        self.horizontalLayout_7.addWidget(self.lblOFFSetPoint)
        self.btnOFFSetPoint = QtWidgets.QPushButton(self.SetPointFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOFFSetPoint.sizePolicy().hasHeightForWidth())
        self.btnOFFSetPoint.setSizePolicy(sizePolicy)
        self.btnOFFSetPoint.setMinimumSize(QtCore.QSize(110, 85))
        self.btnOFFSetPoint.setStyleSheet("background-color:\'royal blue\';color:\'gold\';border-radius:10px;font-size:16px;")
        self.btnOFFSetPoint.setObjectName("btnOFFSetPoint")
        self.horizontalLayout_7.addWidget(self.btnOFFSetPoint)
        self.verticalLayout.addWidget(self.SetPointFrame_2)
        self.gridLayout.addWidget(self.ControlFrame, 2, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 2, 2, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(128, 125, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 3, 1, 1, 1)

        self.retranslateUi(Control)
        QtCore.QMetaObject.connectSlotsByName(Control)

    def retranslateUi(self, Control):
        _translate = QtCore.QCoreApplication.translate
        Control.setWindowTitle(_translate("Control", "Form"))
        self.lblRelay.setText(_translate("Control", "Relay"))
        self.btnRelayNumber.setText(_translate("Control", "1"))
        self.btnENDISABLE.setText(_translate("Control", "ENABLE"))
        self.btnHome.setText(_translate("Control", "Home"))
        self.btnTemperature.setText(_translate("Control", "Temperature"))
        self.btnHumidity.setText(_translate("Control", "Humidity"))
        self.btnManualControl.setText(_translate("Control", "Manual\n"
"Control"))
        self.lblTime.setText(_translate("Control", "10-10-2019 17:06:21"))
        self.lblType.setText(_translate("Control", "Control On"))
        self.cbxType.setItemText(0, _translate("Control", "Temperature"))
        self.cbxType.setItemText(1, _translate("Control", "Humidity"))
        self.lblOnSetPoint.setText(_translate("Control", "ON Set Point:"))
        self.btnONSetPoint.setText(_translate("Control", "10`C"))
        self.lblOFFSetPoint.setText(_translate("Control", "OFF Set Point:"))
        self.btnOFFSetPoint.setText(_translate("Control", "10`C"))


        ############################################################
        #############################################################
        self.updateTime()
        self.startTimeUpdateTimer()
        self.fetchSettingsFromDatabase()
        self.btnHome.clicked.connect(self.open_home_screen)
        self.btnTemperature.clicked.connect(self.open_temp_screen)
        self.btnHumidity.clicked.connect(self.open_humidity_screen)
        self.btnManualControl.clicked.connect(self.open_manuel_control)
        self.btnENDISABLE.clicked.connect(self.en_dis_relay)
        self.btnONSetPoint.clicked.connect(self.setting_point)
        self.btnOFFSetPoint.clicked.connect(self.off_setting_point)
        self.cbxType.currentIndexChanged.connect(self.on_compo_change)
        self.btnRelayNumber.clicked.connect(self.select_relay)


    def open_home_screen(self):
        globals.control.hide()
        globals.Home.show()

    def open_temp_screen(self):
        globals.control.hide()
        globals.temp.show()
    
    def open_humidity_screen(self):
        globals.control.hide()
        globals.humidity.show()

    def open_manuel_control(self):
        globals.control.hide()
        globals.manuel.show()




    def select_relay(self):
        sender = self.sender()
        globals.control.setEnabled(False)

        self.exPopup = numberPopup(globals.control,sender, "",self.verifyInput, sender)
        self.exPopup.setGeometry(200,70,400, 300)
        self.exPopup.show()


    def setting_point(self):
        sender = self.sender()
        globals.control.setEnabled(False)
        self.prev_value= globals.getIntFromStr(self.btnOFFSetPoint.text())

        self.exPopup = numberPopup(globals.control,sender, "",self.verifyInput, sender)
        self.exPopup.setGeometry(200,70,400, 300)
        self.exPopup.show()

    def off_setting_point (self):
        sender = self.sender()
        globals.control.setEnabled(False)
        self.prev_value= globals.getIntFromStr(self.btnOFFSetPoint.text())

        self.exPopup = numberPopup(globals.control,sender, "",self.verifyInput, sender)
        self.exPopup.setGeometry(200,70,400, 300)
        self.exPopup.show()


        
    def on_compo_change(self,value):
        # 0 for temp and 1 for humidity
        database.updateDB("UPDATE settings SET sensor_type = %d WHERE relay_id = %d" % (int(value),int(self.btnRelayNumber.text())))
        self.btnENDISABLE.setStyleSheet("background-color:\'red\';\n"
"color:\'gold\';border-radius:10px;font-size:16px;")
        database.updateDB("UPDATE settings SET enable = 1 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
        self.btnENDISABLE.setText("enable")
        if int(value) == 0:
            database.updateDB("UPDATE settings SET on_value = 20 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            self.btnONSetPoint.setText("20 `C")
            database.updateDB("UPDATE settings SET off_value = 17 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            self.btnOFFSetPoint.setText("17 `C")
        if int(value) == 1:
            database.updateDB("UPDATE settings SET on_value = 35 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            self.btnONSetPoint.setText(" 35 %")
            database.updateDB("UPDATE settings SET off_value = 30 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            self.btnOFFSetPoint.setText(" 30 %")


        




        


    def en_dis_relay(self):
        if self.sender().text()=="ENABLE":
            self.btnENDISABLE.setStyleSheet("background-color:\'red\';\n"
"color:\'gold\';border-radius:10px;font-size:16px;")
            database.updateDB("UPDATE settings SET enable = 0 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            self.sender().setText("DISABLE")
            relay_settings=database.selectOne("SELECT * from settings WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            


        else:
            self.btnENDISABLE.setStyleSheet("background-color:\'green\';\n"
"color:\'gold\';border-radius:10px;font-size:16px;")
            database.updateDB("UPDATE settings SET enable = 1 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            self.sender().setText("ENABLE")
            # if relay is on and automatic control active not manual
            relay_settings=database.selectOne("SELECT * from settings WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
            if relay_settings[6] == 0 and relay_settings[5]==1:
                relay_off(int(self.btnRelayNumber.text()))
                database.updateDB("UPDATE settings SET status = 0 WHERE relay_id = %d" % (int(self.btnRelayNumber.text())))
                

            #database.updateDB("UPDATE programs SET enable = 1 WHERE id = %d" % (int(self.pro_no.text())))
        

    def verifyInput (self,object_sender):
        if object_sender.objectName() == "btnRelayNumber":
            if int(object_sender.text()) > globals.number_of_relays:
                 self.show_error_msg("more than allowed number of relays")
                 object_sender.setText("1")
        
        if object_sender.objectName() == "btnONSetPoint":
            
            if  globals.getIntFromStr(object_sender.text()) <= globals.getIntFromStr(self.btnOFFSetPoint.text())+1:
                self.show_error_msg("must be more than off value") 
                if self.cbxType.currentIndex==0:
                    self.btnONSetPoint.setText("%d `C" %self.prev_value)
                if self.cbxType.currentIndex==0:
                    self.btnONSetPoint.setText("%d" % self.prev_value+" %")
        
            


            else:
                database.updateDB("UPDATE settings SET on_value = %d WHERE relay_id = %d" % ( globals.getIntFromStr(object_sender.text()),int(self.btnRelayNumber.text())))
        


        if object_sender.objectName() == "btnOFFSetPoint":
            if globals.getIntFromStr(object_sender.text()) >= globals.getIntFromStr(self.btnONSetPoint.text())-1 :
                self.show_error_msg("must be less than on value") 
                if self.cbxType.currentIndex==0:
                    self.btnOFFSetPoint.setText("%d `C" %self.prev_value)
                if self.cbxType.currentIndex==0:
                    self.btnOFFSetPoint.setText("%d" % self.prev_value+" %")

            else:
                database.updateDB("UPDATE settings SET off_value = %d WHERE relay_id = %d" % (globals.getIntFromStr(object_sender.text()),int(self.btnRelayNumber.text())))

            

        self.fetchSettingsFromDatabase()
                

    ## This function is used to fetch all the data from the database for the current relay number and update the UI accordingly 
    #
    # @param self The object pointer
    def fetchSettingsFromDatabase(self):
        id = int(self.btnRelayNumber.text())
        if id <= globals.number_of_relays:
            relay_settings=database.selectOne("SELECT * from settings WHERE relay_id = %d" % id) 
            
            if relay_settings[1]==0:
                self.btnENDISABLE.setStyleSheet("background-color:\'red\';\n"
    "color:\'gold\';border-radius:10px;font-size:16px;")
                self.btnENDISABLE.setText("DISABLE")
            else:
                self.btnENDISABLE.setStyleSheet("background-color:\'green\';\n"
    "color:\'gold\';border-radius:10px;font-size:16px;")
                self.btnENDISABLE.setText("ENABLE")

            if relay_settings[2]==0:
                self.cbxType.setCurrentIndex(0)
                self.btnONSetPoint.setText("%d `C" % relay_settings[3])
                self.btnOFFSetPoint.setText("%d `C" % relay_settings[4])

            else:
                self.cbxType.setCurrentIndex(1)
                self.btnONSetPoint.setText("%d" % relay_settings[3]+" %")
                self.btnOFFSetPoint.setText("%d" % relay_settings[4]+" %")

            if relay_settings[5] == 0:
                self.lblONIcon.setPixmap(QtGui.QPixmap("/home/pi/dht/OFFresized.png"))
            else :
                self.lblONIcon.setPixmap(QtGui.QPixmap("/home/pi/dht/ONresized.png"))

        
            

        
            


        




    ## This function is used to show an error message
    # @param errmsg The message that will appear
    def show_error_msg(self, errmsg): 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ERROR")
        msg.setInformativeText(errmsg)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
            

        
        
    def updateTime(self):
            now = datetime.now()
            # H:M:S - DD/MM/YY
            dt_string = now.strftime("%H:%M:%S %d-%b-%Y")
            self.lblTime.setText(dt_string)
            self.fetchSettingsFromDatabase()

    def startTimeUpdateTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000) 



        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Control = QtWidgets.QWidget()
    ui = Ui_Control()
    ui.setupUi(Control)
    Control.show()
    sys.exit(app.exec_())
