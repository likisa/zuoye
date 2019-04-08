import os
import socket


dir_name = os.path.dirname(__file__)

jpg_name = os.path.join(dir_name, '1.jpg')
jpg_name1 = os.path.join(dir_name, '1_copy1.jpg')

with open(jpg_name,'rb') as f:
    b_file = f.read()

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('127.0.0.1',60000)

ss.connect(addr)

ss.sendall(b_file)

ss.close()
