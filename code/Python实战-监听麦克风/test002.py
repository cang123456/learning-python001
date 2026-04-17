
import socket
import time

import pyaudio

format_ = pyaudio.paInt16
channels = 1 # 声道
rate = 44100 # 比率，hz，速度
chunk = 1024 # 数据块

S = socket.socket()             # 创建套接字
S.bind(('0.0.0.0', 8848))       # 绑定端口
S.listen()                      # 开启监听

# s, addr = S.accept()             # 接受连接申请




def play_audio(s):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format_, channels=channels, rate=rate, output=True,
                        frames_per_buffer=chunk, input_device_index=0)  # 打开音频输入流

    while True:
        try:
            data = s.recv(1024)

            stream.write(data)
            # 2. 打开音频文件（追加模式保存原始PCM数据，后续可转MP3）
            audio_file = open('test.pcm', 'ab')  # 'ab'=二进制追加模式，不会覆盖
            audio_file.write(data)
            # 3. 设置Socket超时，避免阻塞
            s.settimeout(5)
        except:                  # 1. 开始没连上   2. 最后断了
            continue



while True:
    s, addr = S.accept()
    print(f'鱼儿来了', addr)
    play_audio(s)
































