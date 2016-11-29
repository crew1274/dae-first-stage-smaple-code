import serial
import RPi.GPIO as GPIO

ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1 )
tr = 18
str1= b'\x01\x03\x60\x90\x00\x0C\x5B\xE2'
#strarr = bytearray([0x01, 0x03, 0x60, 0x90, 0x00, 0x0C, 0x5B, 0xe2])
#strarr = bytearray([1, 16, 160, 0, 0, 3, 6, 4,60,1,1,4,0,231,255])
strarr = bytearray([1, 3, 160, 0, 0, 3, 39,203 ])
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(tr, GPIO.OUT)
GPIO.output(tr, GPIO.LOW)
ser.write(strarr)
ser.flush()
#ser.write(bytearray[0x01])
GPIO.output(tr, GPIO.HIGH)
str2=ser.readlines()
print (str2)





