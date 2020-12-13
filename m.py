import serial
import time
ser =serial.Serial('/dev/ttyACM1',9600)
while 1:
  x=ser.readline()
  msg = 't'
  print(x)
  ser.write(msg.encode())
  time.sleep(1)
