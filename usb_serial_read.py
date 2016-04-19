import serial
import os

# reads serial input on for USB to serial port
# writes to a temporary file that will use the data

#print 'Quick test app for usb'
#print 'Enter the port to check - case sensitive as below'
#print '/dev/ttyUSB0 - for serial to usb converter'
#print '/dev/ttyAMA0 - for gpio to serial connection'
#print 'eg:'
#print '/dev/ttyUSB0'
#port = raw_input()

port = '/dev/ttyUSB0'
homedir = '/home/pi/scans/'

print 'checking on port ', port

ser = serial.Serial(port, \
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=1)

print ser

while True:
        str1 = ser.readline()
        if str1 != '':
                print str1
                fi = open(homedir + str1.rstrip(),"w")
                fi.close()
