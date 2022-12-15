import serial
import os, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
port = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

port.write(b'AT\r')
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write(b'AT+CMGF=1\r')
print('Text Mode Enabled…')
time.sleep(1)
port.write(b'AT+CMGS="+639614335484"\r')
msg = 'test message from SIM900A.'
print('sending message….')
time.sleep(1)
port.reset_output_buffer()
time.sleep(1)
port.write(str.encode(msg+chr(26)))
rcv = port.read(200)
print(rcv)
time.sleep(1)
print('message sent…')
