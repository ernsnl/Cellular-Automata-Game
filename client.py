# Echo client program
from threading import Thread
import socket
import sys

HOST = '50.17.57.209'    # The remote host
PORT = 4758              # The same port as used by the server
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)

def client_send(s):
    try:
        while True:
            print 'Waiting your input:'
            _input = raw_input()
            s.sendall(_input)
    except Exception as e:
        s.close()

def client_read(s):
    try:
        while True:
            data = s.recv(1024)
            print 'Received', repr(data)
    except Exception as e:
        s.close()

send_data = Thread(target=client_send, args=(s, ))
send_data.start()
receive_data =  Thread(target=client_read, args=(s, ))
receive_data.start()

send_data.join()
receive_data.join()
