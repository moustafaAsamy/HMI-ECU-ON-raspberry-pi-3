  #!/usr/bin/env python   
      
import time
import serial
               
ser = serial.Serial(            
     port='/dev/serial0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=1)
msg = 'toot\n'



counter =1
while 1:
     ser.write(msg.encode())
     #time.sleep(0.1)
     
          #ser.write(msg.encode())
     #rmsg = ser.read(1)
     #print( counter )
     #nc =ser.inWaiting()
     #print (nc)
     #if nc > 0:
         # rmsg = ser.readline()
     #counter=counter+1
         # print (rmsg )
          #print('\n')
     #print (rmsg )
