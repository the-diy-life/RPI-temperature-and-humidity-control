# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow #this is to enable the self.sender function

from PyQt5.QtCore import QTimer
from datetime import datetime, timezone, timedelta
import time

import globals

import threading
import Adafruit_DHT
import database

import os

from relay_lib_seeed import *




class Ui_Home(QMainWindow):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Home)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setObjectName("gridLayout")
        self.btnControlCenter = QtWidgets.QPushButton(Home)
        self.btnControlCenter.setStyleSheet("background-color:\'royal blue\';color:\'gold\';padding:30px;border-radius:10px;font-size:16px;")
        self.btnControlCenter.setObjectName("btnControlCenter")
        self.gridLayout.addWidget(self.btnControlCenter, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labWelcomeMessage = QtWidgets.QLabel(Home)
        self.labWelcomeMessage.setStyleSheet("#labWelcomeMessage{\n"
"font-size:24px;\n"
"color:gold;\n"
"font-weight:bold;\n"
"}")
        self.labWelcomeMessage.setObjectName("labWelcomeMessage")
        self.horizontalLayout.addWidget(self.labWelcomeMessage)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.btnShutDown = QtWidgets.QPushButton(Home)
        self.btnShutDown.setStyleSheet("background-color:\'royal blue\';color:\'gold\';padding:30px;border-radius:10px;font-size:16px;")
        self.btnShutDown.setObjectName("btnShutDown")
        self.gridLayout.addWidget(self.btnShutDown, 6, 1, 1, 1)
        self.btnManualControl = QtWidgets.QPushButton(Home)
        self.btnManualControl.setStyleSheet("background-color:\'royal blue\';color:\'gold\';padding:30px;border-radius:10px;font-size:16px;")
        self.btnManualControl.setObjectName("btnManualControl")
        self.gridLayout.addWidget(self.btnManualControl, 4, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lblTime = QtWidgets.QLabel(Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTime.sizePolicy().hasHeightForWidth())
        self.lblTime.setSizePolicy(sizePolicy)
        self.lblTime.setMaximumSize(QtCore.QSize(200, 21))
        self.lblTime.setStyleSheet("#lblTime\n"
"{\n"
"qproperty-alignment:AlignCenter;\n"
"background-color:White;\n"
"color:blue;\n"
"font-size:12px;\n"
"font-weight:bold;\n"
"\n"
"\n"
"}")
        self.lblTime.setObjectName("lblTime")
        self.horizontalLayout_2.addWidget(self.lblTime)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 3, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.btnDisplayHumi = QtWidgets.QPushButton(Home)
        self.btnDisplayHumi.setStyleSheet("background-color:\'royal blue\';color:\'gold\';padding:30px;border-radius:10px;font-size:16px;")
        self.btnDisplayHumi.setObjectName("btnDisplayHumi")
        self.gridLayout.addWidget(self.btnDisplayHumi, 2, 3, 1, 1)
        self.labLogo = QtWidgets.QLabel(Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labLogo.sizePolicy().hasHeightForWidth())
        self.labLogo.setSizePolicy(sizePolicy)
        self.labLogo.setMaximumSize(QtCore.QSize(129, 129))
        self.labLogo.setText("")
        self.labLogo.setPixmap(QtGui.QPixmap("/home/pi/dht/TheDIYLifeLogo.png"))
        self.labLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labLogo.setWordWrap(True)
        self.labLogo.setObjectName("labLogo")
        self.gridLayout.addWidget(self.labLogo, 0, 4, 1, 1)
        self.btnDisplayTemp = QtWidgets.QPushButton(Home)
        self.btnDisplayTemp.setStyleSheet("background-color:\'royal blue\';color:\'gold\';padding:30px;border-radius:10px;font-size:16px;")
        self.btnDisplayTemp.setObjectName("btnDisplayTemp")
        self.gridLayout.addWidget(self.btnDisplayTemp, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 5, 1, 1, 1)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.btnControlCenter.setText(_translate("Home", "Control Center"))
        self.labWelcomeMessage.setText(_translate("Home", "Welcome To The DIY Life Show Case"))
        self.btnShutDown.setText(_translate("Home", "Shut Down"))
        self.btnManualControl.setText(_translate("Home", "Manual Control"))
        self.lblTime.setText(_translate("Home", "10-10-2019 17:06:21"))
        self.btnDisplayHumi.setText(_translate("Home", "Display Humidity"))
        self.btnDisplayTemp.setText(_translate("Home", "Display Temperature"))


        #########################################################
        self.updateTime()
        self.startTimeUpdateTimer()
        self.btnDisplayTemp.clicked.connect(self.open_temp_screen)
        self.btnDisplayHumi.clicked.connect(self.open_humidity_screen)
        self.btnManualControl.clicked.connect(self.open_manuel_control)
        self.btnControlCenter.clicked.connect(self.open_control_screen)

        # ---------------------------------------------------------------------
        # Shutdown button implementation (hold)
        # ---------------------------------------------------------------------
        self.btnShutDown.pressed.connect(self.shutdown_pressed)
        self.btnShutDown.released.connect(self.shutdown_released)
        self.shutdown_button_timer = QTimer()
        self.shutdown_button_timer.timeout.connect(self.shutdown_button_event_check)
        self.shutdown_button_held_time = 0
        # ---------------------------------------------------------------------




    def open_control_screen(self):
        globals.control.show()

    def open_temp_screen(self):
        globals.temp.show()
    
    def open_humidity_screen(self):
        globals.humidity.show()
    
    def open_manuel_control(self):
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

             
    ## shutdown button pressed handler
    def shutdown_pressed(self):
        self.shutdown_button_timer.start(50)

    ## shutdown button released handler
    def shutdown_released(self):
        self.shutdown_button_timer.stop()
        self.shutdown_button_held_time = 0 


    # shutdown button hold for 5 seconds implementation
    def shutdown_button_event_check(self):
        self.shutdown_button_held_time += 0.05
        if self.shutdown_button_held_time >= 5: 
            self.shutdown_button_timer.stop()
            self.shutdown_button_held_time = 0 
            os.system("sudo shutdown -h now")

def main_loop():
    n1 = datetime.now()
    

    while 1:
        
        time.sleep(5)
        
        globals.humidity_read, globals.temperature_read = Adafruit_DHT.read_retry(globals.DHT_SENSOR, globals.DHT_PIN)
        
        now = datetime.now()

        now_timestamp=datetime.timestamp(now)
        #print(now_timestamp)
        #print(datetime.timestamp(n1))
        #print(globals.temperature_read)
        if now_timestamp - datetime.timestamp(n1) > 9: # globals.read_interval:
           
            if now.day>n1.day:
                # delete records every day
                database.updateDB("TRUNCATE TABLE temp_log")
                database.updateDB("TRUNCATE TABLE humidity_log")
                globals.temp_list_date.append(now_timestamp)
                globals.temp_list_value.append(int(globals.temperature_read))

                globals.humidity_list_date.append(now_timestamp)
                globals.humidity_list_value.append(int(globals.humidity_read))

        
            n1=now

            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            
            database.updateDB('INSERT INTO temp_log (time, value) VALUES ( "%s", %d)' % (formatted_date,int(globals.temperature_read)))
            database.updateDB('INSERT INTO humidity_log (time, value) VALUES ( "%s", %d)' % (formatted_date,int(globals.humidity_read)))
            print("success write to db")
            
            globals.temp_list_date.append(now_timestamp)
            globals.temp_list_value.append(int(globals.temperature_read))

            globals.humidity_list_date.append(now_timestamp)
            globals.humidity_list_value.append(int(globals.humidity_read))

        

def perform_shots():
    while 1:
        for i in range(globals.number_of_relays):

            relay_settings=database.selectOne("SELECT * from settings WHERE relay_id = %d" % (i+1)) 
            if relay_settings[1]==0 and relay_settings[6]==0:
                if relay_settings[2]==0:
                    if globals.temperature_read >= relay_settings[3] and relay_settings[5]==0:
                    
                        relay_on(i+1)
                        database.updateDB("UPDATE settings SET status = 1 WHERE relay_id = %d" % (i+1))

                    if globals.temperature_read <= relay_settings[4] and relay_settings[5]==1:
                         relay_off(i+1)
                         database.updateDB("UPDATE settings SET status = 0 WHERE relay_id = %d" % (i+1))

                if relay_settings[2]==1:
                    if globals.humidity_read >= relay_settings[3] and relay_settings[5]==0:
                    
                        relay_on(i+1)
                        database.updateDB("UPDATE settings SET status = 1 WHERE relay_id = %d" % (i+1))

                    if globals.humidity_read <= relay_settings[4] and relay_settings[5]==1:
                         relay_off(i+1)
                         database.updateDB("UPDATE settings SET status = 0 WHERE relay_id = %d" % (i+1))
                
            if relay_settings[1]==1 and relay_settings[5]==1 and relay_settings[5]==0 :
                relay_off(i+1)
                database.updateDB("UPDATE settings SET status = 0 WHERE relay_id = %d" % (i+1))


        


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    globals.initialize()
    
    globals.Home.show()
    threading.Thread(target=main_loop, daemon=True).start()
    threading.Thread(target=perform_shots, daemon=True).start()
    sys.exit(app.exec_())
