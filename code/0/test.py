import pyaudio, queue, socket, threading

s = socket.socket()  # 创建一个套接字
s.connect(('146.56.223.48', 8848))  # 申请连接后台

audio_queue = queue.Queue()  # 初始队列 用于存放音频数据 保证线程安全


# 录音线程函数
def record_audio():
    print('创建实例！')
    audio = pyaudio.PyAudio()  # 初始化pyaudio的对象 程序里面招过来的一个音响师！ 工位0
    print('打开音频流')
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                        frames_per_buffer=1024, input_device_index=0)  # 打开音频输入(录制)输出(播放)流

    while True:  # 循环录制
        data = stream.read(1024)  # 从音频流中读取数据
        audio_queue.put(data)  # 把数据放到队列里面


# 发送音频数据
def send_audio(s):
    while True:
        try:
            data = audio_queue.get()
            s.send(data)
        except:
            continue


thread1 = threading.Thread(target=record_audio)
thread1.start()
thread2 = threading.Thread(target=send_audio, args=(s,))
thread2.start()