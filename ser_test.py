import serial

import time

import RPi.GPIO as GPIO



from  rs485 import *

from  myfunction import *



ser = serial.Serial(

        '/dev/ttyAMA0',

        baudrate=9600,

        bytesize=8,

        stopbits=1,

        timeout=1

)



sendStr1 = "\x01\x03\x60\x90\x00\x0c\x5b\xe2"

sendStr2 = bytearray(b"\x01\x03\x60\x90\x00\x0C\x5B\xE2")



print "set gpio"



GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)



print "------------ serial  ----------"

print ser

print ser.isOpen()



getResponse(ser, sendStr1)

getResponse(ser, sendStr2)

getResponse(ser, b"\x01\x03\x60\x90\x00\x0C\x5B\xE2")

ser.close()

print "serial is close."



print "\n-------------- rs485 ------------------------"

rs = RS485('/dev/ttyAMA0',

        baudrate=9600,

        bytesize=8,

        stopbits=1,

        timeout=1

)

print rs

print rs.isOpen()

getResponse(rs, sendStr1)

getResponse(rs, sendStr2)

getResponse(rs, b"\x01\x03\x60\x90\x00\x0C\x5B\xE2")

rs.close()

print "rs485 is close."