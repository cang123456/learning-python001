from socket import *
import os

s = socket()

s.connect(('127.0.0.1',8888))

choice = s.recv(1024).decode()

if choice == '1':
    os.system('shutdown -s -t 60')
elif choice == '2':
    os.system('shutdown -r -t 60')
elif choice == '3':
    print(3)