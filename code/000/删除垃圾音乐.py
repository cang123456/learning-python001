import os
from mutagen.mp3 import MP3
from mutagen import MutagenError

# 👇 这里改成你的音乐文件夹路径
MUSIC_DIR = r"D:\project\2026\forme001\forme001\wms-web\public\music"


def scan_and_delete_bad_mp3():
    for filename in os.listdir(MUSIC_DIR):
        if filename.endswith(".mp3"):
            path = os.path.join(MUSIC_DIR, filename)

            try:
                # 尝试读取音频信息 → 坏文件/加密文件会报错
                audio = MP3(path)
                duration = audio.info.length
                print(f"✅ 正常：{filename}，时长：{duration:.1f}s")

            except (MutagenError, Exception) as e:
                # 报错 = 损坏 / 加密 / 无法播放
                print(f"❌ 坏文件/加密，已删除：{filename}")
                os.remove(path)


if __name__ == '__main__':
    scan_and_delete_bad_mp3()