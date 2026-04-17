import socket
import queue
import threading

import pyaudio

destination_ip_port = ('127.0.0.1',8848) # 目的ip 端口
format_ = pyaudio.paInt16
channels = 1 # 声道
rate = 44100 # 比率，hz，速度
chunk = 1024 # 数据块
q = queue.Queue() # 存储数据


s = socket.socket()
s.connect(destination_ip_port)

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format_,channels=channels,rate=rate,input=True,
               frames_per_buffer=chunk, input_device_index=0) # 打开音频输入流
    while True:
        data = stream.read(1024)
        q.put(data)

def send_audio(s):
    while True:
        if not q.empty():
            s.send(q.get())

thread1 = threading.Thread(target=record_audio)
thread2 = threading.Thread(target=send_audio, args=(s,))
thread1.start()
thread2.start()






















# audio_monitoring