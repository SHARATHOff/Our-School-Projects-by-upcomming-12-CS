import socket


host ='127.0.0.1'  # Standard loopback interface address 

port = 6543        # Port to listen on (non-privileged ports are > 1023)

serv = socket.socket()

serv.bind((host, port))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    conn.send(b"Attack ")
    data = conn.recv(4096)
    if not data: break
    print (data)