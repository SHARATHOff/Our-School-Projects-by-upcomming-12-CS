import socket as st
con=st.socket()
clients=[]
connections=[]
con.bind(('127.0.0.5',8000))
i=0
while i < 2 :
    con.listen()
    a,addr=con.accept()
    clients.append(addr)
    connections.append(a)
    
    i+=1
    a.send(bytes(f'{clients}'.encode()))
print(clients)
    


for connection in connections:
    connection.send(bytes('choose the other client'.encode()))
while True:
    for connection in connections:
        
        try:
            recieved=connection.recv(1024)
            print(recieved.decode())
        except:
            pass
    
    '''q=input('enter')
    a.send(f"server{q}".encode())
    c=a.recv(1024)
    c=c.decode()
    print(c)'''
