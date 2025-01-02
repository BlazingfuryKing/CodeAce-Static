#Task 1.3
#client.py - with validity check on user inputs (5 marks)

from socket import socket

my_socket = socket()

my_socket.connect(('127.0.0.1', 12345))     #connect to server [1]

for i in range(5):
    data = my_socket.recv(1024).decode()    # able to print server msg [1] 
    print(data)
    while True:
        xloc = input('Enter x location (0-5) : ')
        if xloc.isdigit() and 0<=int(xloc)<=5:
            break
    
    while True:
        yloc = input('Enter y location (0-5) : ')
        if yloc.isdigit() and 0<=int(yloc)<=5:
            break
        
    loc = xloc + yloc                        #send xloc and yloc [1]
    my_socket.sendall(loc.encode())          #send user input [1]
   
data = my_socket.recv(1024).decode()
print(data)      

my_socket.close()                    # close client [1]


