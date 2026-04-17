from socket import*
import time

S = socket()
S.bind(('0.0.0.0', 4321))
S.listen()


def online_sb(addr):
    print(f"{addr[0]}已连接")
    print("请输入指令shutdown restart warning")


# # 错误代码---无法正常循环，自己断开了链接
# while True:
#     s, addr = S.accept()
#     online_sb(addr)
#     while True:
#         cmd = input("输入指令：")
#         try:
#             s.send(cmd.encode())
#         except:
#             break
#         if cmd in ['shutdown', 'restart', 'warning']:
#             print(addr[0],s.recv(1024).decode())
#             break

while True:
    s, addr = S.accept()
    online_sb(addr)
    # 与当前客户端的通信循环（保持持续通信）
    while True:
        cmd = input("输入指令: ")
        try:
            s.send(cmd.encode())
            # 仅当指令是指定类型时，接收客户端的回复（不break）
            if cmd in ['shutdown', 'restart', 'warning']:
                print(addr[0], s.recv(1024).decode())
        except:
            print(f"{addr[0]}断开连接")
            break  # 只有客户端断开时，才跳出通信循环