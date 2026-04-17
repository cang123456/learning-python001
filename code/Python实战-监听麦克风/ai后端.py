import pyaudio
import socket
import traceback

# 定义音频参数（统一播放/录制/传输格式）
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024


def play_audio(s, exit_event):
    """
    播放从Socket接收的音频数据，并保存原始PCM音频文件
    :param s: 客户端Socket连接
    :param exit_event: 退出事件（threading.Event），用于优雅停止
    """
    audio = None
    stream = None
    audio_file = None
    try:
        # 1. 初始化PyAudio和播放流（移除错误的input_device_index）
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            output=True,  # 播放模式
            frames_per_buffer=CHUNK
        )
        # 2. 打开音频文件（追加模式保存原始PCM数据，后续可转MP3）
        audio_file = open('test.pcm', 'ab')  # 'ab'=二进制追加模式，不会覆盖

        # 3. 设置Socket超时，避免阻塞
        s.settimeout(5)

        print("开始播放音频，同时保存原始PCM数据到test.pcm...")
        while not exit_event.is_set():
            try:
                # 接收音频数据
                data = s.recv(CHUNK)

                # 处理客户端正常断开
                if not data:
                    print("客户端正常断开连接")
                    break

                # 播放音频
                stream.write(data)

                # 保存原始PCM数据（二进制直接写入，无需decode）
                audio_file.write(data)

            except socket.timeout:
                # recv超时，继续循环（避免卡死）
                continue
            except Exception as e:
                print(f"音频播放/保存出错: {e}")
                traceback.print_exc()  # 打印详细错误栈，方便调试
                break  # 出错后退出循环，避免无限报错

    except Exception as e:
        print(f"初始化音频/文件失败: {e}")
        traceback.print_exc()
    finally:
        # 4. 确保所有资源优雅释放
        if audio_file:
            audio_file.close()
            print("音频文件已关闭（test.pcm）")
        if stream:
            stream.stop_stream()
            stream.close()
            print("音频播放流已关闭")
        if audio:
            audio.terminate()
            print("PyAudio资源已释放")
        if s:
            try:
                s.close()
                print("Socket连接已关闭")
            except:
                pass


# ------------------- 测试使用示例 -------------------
if __name__ == "__main__":
    import threading

    # 创建退出事件（用于优雅停止）
    exit_event = threading.Event()

    # 初始化服务器Socket（模拟接收端）
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 8848))
    server_socket.listen(1)
    print("等待客户端连接...")

    try:
        # 等待客户端连接
        client_sock, addr = server_socket.accept()
        print(f"客户端已连接: {addr}")

        # 启动播放音频线程
        play_thread = threading.Thread(target=play_audio, args=(client_sock, exit_event))
        play_thread.start()

        # 按回车停止程序
        input("按回车键停止播放...\n")
        exit_event.set()  # 设置退出标志
        play_thread.join()  # 等待线程退出

    finally:
        server_socket.close()
        print("服务器Socket已关闭")