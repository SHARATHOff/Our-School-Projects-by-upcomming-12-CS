import socket as st
import time
con=st.socket()

con.connect(('127.0.0.5',9999))
i=0
'''while i<2:
    a=con.recv(1024)
    a=a.decode()
    print(a)
    i+=1'''
while True:
    q=input('enter')
    print(q)
    con.send(bytes(f'{q}'.encode()))
    
