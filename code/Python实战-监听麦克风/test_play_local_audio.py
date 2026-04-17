import pyaudio

format_ = pyaudio.paInt16
channels = 1 # 声道
rate = 44100 # 比率，hz，速度
chunk = 1024 # 数据块


# ffmpeg -y -f s16le -ar 44100 -ac 1 -i test.pcm -codec:a libmp3lame -b:a 128k test.mp3

def play_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format_, channels=channels, rate=rate, output=True,
                        frames_per_buffer=chunk, input_device_index=0)  # 打开音频输入流
    with open('test.pcm','rb') as f:
        stream.write(f.read())



play_audio()















