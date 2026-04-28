import os
import requests
import time
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# -------------------------- 配置区 --------------------------
BASE_URL = "http://119.29.206.197/music/"
SAVE_DIR = "bgm_music"
START_NUM = 1
END_NUM = 607
THREADS = 32  # 线程数，16 最稳，可改 8/24/32
TIMEOUT = 15
RETRY_COUNT = 3
# -----------------------------------------------------------

# 屏蔽警告
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

# 创建保存目录
os.makedirs(SAVE_DIR, exist_ok=True)

# 全局请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "http://119.29.206.197/"
}

def download_one_song(num):
    """下载单首音乐（线程安全）"""
    filename = f"mus{num}.mp3"
    url = BASE_URL + filename
    save_path = os.path.join(SAVE_DIR, filename)

    # 已下载直接跳过
    if os.path.exists(save_path):
        return True, filename

    # 重试机制
    for _ in range(RETRY_COUNT):
        try:
            resp = requests.get(
                url,
                stream=True,
                timeout=TIMEOUT,
                headers=HEADERS,
                verify=False
            )
            if resp.status_code == 200:
                total = int(resp.headers.get("content-length", 0))
                with open(save_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=1024 * 64):
                        f.write(chunk)
                return True, filename
        except Exception:
            time.sleep(0.5)

    return False, filename

def multi_thread_download():
    """多线程批量下载"""
    print(f"🚀 多线程下载 {START_NUM}~{END_NUM} 首音乐")
    print(f"🧵 线程数：{THREADS}")
    print(f"💾 保存到：{os.path.abspath(SAVE_DIR)}\n")

    tasks = list(range(START_NUM, END_NUM + 1))
    success = 0
    fail_list = []

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        future_map = {executor.submit(download_one_song, num): num for num in tasks}

        for future in tqdm(as_completed(future_map), total=len(tasks), desc="整体进度"):
            ok, fname = future.result()
            if ok:
                success += 1
            else:
                fail_list.append(future_map[future])

    # 结果
    print("\n" + "=" * 50)
    print(f"✅ 成功：{success} 首")
    print(f"❌ 失败：{len(fail_list)} 首")
    if fail_list:
        print(f"失败序号：{fail_list}")

if __name__ == "__main__":
    multi_thread_download()