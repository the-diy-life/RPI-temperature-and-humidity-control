## @package globals

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Adafruit_DHT
import database
from datetime import datetime

import HomePage
import Humidity
import Temperature
import ControlCenter
import ManualControl



def initialize():

# for temp readings
    global temp_list_date
    global temp_list_value
    temp_list_date=[]
    temp_list_value=[]

    readings =database.selectMany("SELECT * from temp_log") 
    for i in readings:
        temp_list_date.append(datetime.timestamp(i[1]))
        temp_list_value.append(int(i[2]))

# for humidity readings
    global humidity_list_date
    global humidity_list_value
    humidity_list_date=[]
    humidity_list_value=[]

    readings2 =database.selectMany("SELECT * from humidity_log") 
    for i in readings2:
        humidity_list_date.append(datetime.timestamp(i[1]))
        humidity_list_value.append(int(i[2]))



    
    global number_of_relays
    number_of_relays = 4

    global read_interval
    read_interval = 60

    global DHT_SENSOR
    DHT_SENSOR = Adafruit_DHT.DHT11
    global DHT_PIN 
    DHT_PIN = 27

    global temperature_read
    global humidity_read

    humidity_read, temperature_read = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)


    global Home 
    Home = QtWidgets.QWidget()
    global home_screen
    home_screen = HomePage.Ui_Home()
    home_screen.setupUi(Home)

    global control  
    control  = QtWidgets.QWidget()
    global control_screen
    control_screen = ControlCenter.Ui_Control()
    control_screen.setupUi(control)

    global temp  
    temp  = QtWidgets.QWidget()
    global temp_screen
    temp_screen = Temperature.Ui_Temperature()
    temp_screen.setupUi(temp)

    global humidity  
    humidity  = QtWidgets.QWidget()
    global humidity_screen
    humidity_screen = Humidity.Ui_Temperature()
    humidity_screen.setupUi(humidity)

    global manuel  
    manuel  = QtWidgets.QWidget()
    global manuel_screen
    manuel_screen = ManualControl.Ui_Control()
    manuel_screen.setupUi(manuel)
'''
    global temp  
    temp  = QtWidgets.QWidget()
    global temp_screen
    temp_screen = Temperature.Ui_Temperature()
    temp_screen.setupUi(temp)

    global control  
    control  = QtWidgets.QWidget()
    global control_screen
    control_screen = ControlCenter.Ui_Control()
    control_screen.setupUi(control)

    global manuel  
    manuel  = QtWidgets.QWidget()
    global manuel_screen
    manuel_screen = ManualControl.Ui_Control()
    manuel_screen.setupUi(manuel)

'''

## this function gets the number from a string, e.g.: pushButton16 would return 16
def getIntFromStr(strVal):
    return int("".join(filter(str.isdigit, strVal)))