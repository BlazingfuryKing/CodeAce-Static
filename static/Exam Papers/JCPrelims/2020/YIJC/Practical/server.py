#Task 1.3
#server.py (7 marks)

ship = []

with open('GAME.TXT', 'r') as f:
    content = f.readlines()
    row = 0
    for line in content:
        line = line.strip()
        for col in range(len(line)):
            if line[col] == 'X':
                ship.append([col,row])
        row += 1

#print(ship)                            #read and store into ship [1]

from socket import socket

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()                      #initialise socket [1]


new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))     #evidence of connection [1]

sunk = []
missed = []

msg = 'Enter your target location : (x, y) '
new_socket.sendall(msg.encode())            #able to sendall/encode [1]

for i in range(5):

    data = new_socket.recv(1024).decode()     #able to recv/decode [1]
    xloc, yloc = int(data[0]), int(data[1])   #interpret xloc,yloc [1]

    print(xloc,yloc)
    if [xloc,yloc] in ship:
        ship.remove([xloc,yloc])
        sunk.append([xloc,yloc])
    else:
        missed.append([xloc,yloc])

    string = ''
    for row in range(6):
        for col in range(6):
            if i==4 and [col,row] in ship:
                string += 'X' 
            elif [col,row] in sunk:
                string += 'S'
            elif [col,row] in missed:
                string += 'O'
            else:
                string += '.'
        string += '\n'

    new_socket.sendall(string.encode())
  
new_socket.close()                         #close server [1]
my_socket.close()
