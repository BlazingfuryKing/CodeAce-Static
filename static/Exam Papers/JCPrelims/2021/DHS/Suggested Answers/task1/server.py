#server
def generateKey(key, string):
    key = list(key)
    if len(string) == len(key):
        return(key)                  
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])                  
    return("" . join(key))                  

print("Secret key:", generateKey("cat", "hello"))                 


    
def encrypt(password, message):
    new_secret = generateKey(password,message)                 
    
    outcome=[]
    for i in range(len(message)):
        outcome.append(chr(ord(new_secret[i])+ord(message[i])))                 

   
    return "".join(outcome)                  


def decrypt(password, message):
    new_secret = generateKey(password,message)  
    list = []
    for i in range(len(message)):
        list.append(ord(message[i])-ord(new_secret[i]))                 
    
    return "".join([chr(int(i)) for i in list])                 
              
print("Encrypt then Decrypt: ", decrypt("cat", encrypt("cat","hello")))

class Queue:              
    def __init__(self):
        self.Items = [""] * 300
        self.Front = -1
        self.Rear = -1              
    
    def IsEmpty(self):
        return self.Front == -1
    
    def IsFull(self):
        return self.Rear == 265
    
    def enqueue(self, string): 
        if self.IsFull(): #queue is full              
            return "Queue is full!"
        else:
            if self.Front == -1: #queue is empty              
                self.Front += 1
            self.Rear += 1
            self.Items[self.Rear] = string              
            return
            
    def dequeue(self):
        if self.IsEmpty():
            return "Queue is empty!"              
        else:
            item = self.Items[self.Front]
            if self.Front == self.Rear: #last item removed              
                self.Front, self.Rear = -1, -1              
            else:
                self.Front += 1              
            return item              

        
    def display(self):
        if self.IsEmpty():
            return  "queue is empty"            
        else:
            combine = ""
            for i in range(self.Front, self.Rear+1):
                 combine += self.Items[i] + ", "              
            return combine
        
    
    def current_size(self):
        if self.IsEmpty():
            return 0              
        else:
            count = 0
            for i in range(self.Front, self.Rear+1):
                count += 1              
            return count

        
        

q = Queue() 

# Server program

import socket
import random



print("Please set a password:")
server_key = input("Answer:")           
password = server_key 


while True:         
    print(
    '''
Next action?
Menu:
1) Wait for connection from client for next pickup request.
2)Dequeue
Type an option:''')
    response = input()
    
    if response == "1":   
        listen_socket = socket.socket()          
        listen_socket.bind(('127.0.0.1', 9999))         
        listen_socket.listen()         

        print("Awaiting connection from pickup clients...")         
        s, addr = listen_socket.accept()
        print("Connection established!")         
        print("Receiving data from client…")
        
        
        data = b''
        while b'\n' not in data:         
            data += s.recv(1024)         
        data = data[:data.find(b'\n')]         
        
        
        key = decrypt(password, data.decode().split("/")[0])         
        size = decrypt(password, data.decode().split("/")[1])         
        name = decrypt(password, data.decode().split("/")[2])        

        

        print("Checking client's secret key...")
        
        if key == password:
            print("Client's secret key is correct!")
        else:
            print("Wrong secret key")
            msgg = (encrypt(password, "cancelled"))
            msgg=msgg.encode()
            s.sendall(msgg)
            s.close()
            print("Connection disconnected")
            continue    



        print("Client's Team name:", name)
        print("Group size:", size)
        print("No. of passengers in queue:", q.current_size())
        
        new_amount = (int(q.current_size()) + int(size))
        if new_amount > 266:
            print("You do NOT have capacity for them.")
            msgg = (encrypt(password, "cancelled"))
            msgg=msgg.encode()
            s.sendall(msgg)
            s.close()
            print("Connection disconnected")
            continue
        else:
            print("You have capacity for them.")
        print("")
        
       
                           
        print("Confirm pickup? Y/N?")
        ask_pickup = input("Answer:")
        if ask_pickup == "Y":
            [q.enqueue(name) for i in range(int(size))]
            print("Added to queue. Items in queue now are:")
            print(q.display())
        else:
            msgg = (encrypt(password, "cancelled"))
            msgg=msgg.encode()
            s.sendall(msgg)
            s.close()
            print("Connection disconnected")
            continue
            

        msgg = (encrypt(password, "confirmed"))
        msgg=msgg.encode()
        s.sendall(msgg)
        
        
        s.close()         
        print("Connection disconnected")         

        listen_socket.close()         
        
    elif response == "2":
        resp_deq = input("How many to dequeue?")
        for i in range(int(resp_deq)):
            q.dequeue()
        print("Items in queue now are:")
        print(q.display())



