import socket

UDP_PORT = 0
UDP_IP = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
              
sock.bind((UDP_IP, UDP_PORT))

while True:
        print('l')
        data =sock.recvfrom(1024)
        sock.send("hlhkh")
        print(data)
