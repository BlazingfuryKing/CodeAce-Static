#Client

def generateKey(key, string):
    key = list(key)
    if len(string) == len(key):
        return(key)                  
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])                  
    return("" . join(key))                  

print("Secret key:", generateKey("cat", "item"))                 


    
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
              
print("Encrypt then Decrypt: ", decrypt("cat", encrypt("cat","item")))


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

### Test cases for queue
##testq = Queue()
##print(None, testq.enqueue("item1"))
##print(None, testq.enqueue("item2"))
##print(None, testq.enqueue("item3"))
##print(3, testq.current_size())
##print("item1, item2, item3", ":", testq.display())
##print("Queue is full!", testq.enqueue("item4"))
##print(None, testq.dequeue())
##print(None, testq.dequeue())
##print(None, testq.dequeue())
##print("Queue is empty!", testq.dequeue())
##print("Queue is empty!", testq.display())  
        

q = Queue()


# Client program

import socket


print("Please set a password.")
password = input("Answer:")
print()
print("What is your Team Name?")
name = input("Answer:")
print()
print("Group size?")
size = input("Answer:")
print()

encry_key = password

items = [password,size,name]
for i in range(len(items)):
    items[i] = encrypt(encry_key, items[i])

message = "/".join(items)

print("Establishing connection...")
s = socket.socket()
s.connect(('127.0.0.1', 9999))
print("Connection established!")

data = b''

s.sendall(message.encode() + b'\n')
print("Data sent!")

print()
print("Waiting for the server to confirm your request...")
print()
data=s.recv(1024)

decrypted_data = data
decrypted_data = decrypted_data.decode()
print("decrypteddata:",decrypted_data)
decrypted_data = decrypt(password,decrypted_data)
print("decrypteddata:",decrypted_data)

if decrypted_data=="cancelled":
    print("""Pickup cancelled. 
Wrong password or request rejected.
Please try again.""")

if decrypted_data=="confirmed":
    print("""Pickup confirmed! Please wait for pickup to arrive.""")

s.close()
print()
print("Connection disconnected.")
