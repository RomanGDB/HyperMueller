# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:59:02 2020

@author: Rusty Nicovich
"""

import serial
import time

comPort = 'COM3'
baud = 115200
timeOut = 1


    # CONFIGURACION PUERTO SERIAL.
ser = serial.Serial(timeout=4)
ser.port = "COM3"
ser.baudrate = 57600
ser.parity = serial.PARITY_NONE;
ser.stopbits = serial.STOPBITS_ONE;

    # self.ser = serial.Serial('COM4')  # COM4 is the AOTF
print(ser.name)
    # self.ser.baudrate = 57600  # set Baud rate to 57600
    # self.ser.bytesize = 8  # Number of data bits = 8
    # self.ser.parity = 'N'  # No parity
    # self.ser.stopbits = 1  # 1 Stop bits
    # time.sleep(3)


serObj = serial.Serial(comPort, baud, timeout = timeOut)
time.sleep(300)
serObj.flushInput()
serObj.reset_input_buffer()
