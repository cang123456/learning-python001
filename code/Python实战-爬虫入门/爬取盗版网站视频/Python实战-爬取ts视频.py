import m3u8,requests

import m3u8
import requests

# 1. 目标.m3u8文件URL（替换为你抓取到的实际链接）
m3u8_url = "https://vip.dytt-hot.com/20250808/97883_13e02e26/3000k/hls/mixed.m3u8"

# 2. 发送请求获取.m3u8内容（需携带浏览器请求头，避免被识别为爬虫）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://vip.dytt-cinema.com/",  # 来源页URL（必须与播放页一致）
    # "Cookie": "xxx"  # 从浏览器复制登录后的Cookie（若视频需登录）
}

response = requests.get(m3u8_url, headers=headers, timeout=10)
if response.status_code != 200:
    raise Exception(f"获取.m3u8失败，状态码：{response.status_code}")

# 3. 解析.m3u8，提取.ts切片URL（自动处理相对路径）
m3u8_obj = m3u8.loads(response.text)
ts_urls = []
for segment in m3u8_obj.segments:
    # 若.ts是相对路径，拼接成完整URL
    ts_url = segment.uri if segment.uri.startswith("http") else m3u8_url.rsplit("/", 1)[0] + "/" + segment.uri
    ts_urls.append(ts_url)

print(f"成功解析到{len(ts_urls)}个.ts切片URL")


import os
import time
import random
from requests.exceptions import RequestException

# 1. 定义下载目录（避免中文路径）
save_dir = "test"
os.makedirs(save_dir, exist_ok=True)

# 2. 批量下载函数（带重试与延迟）
def download_ts(ts_url, save_path, retry=3):
    for i in range(retry):
        try:
            # 随机延迟（0.5-2秒），模拟人工播放速度
            time.sleep(random.uniform(0.5, 2))
            # 以二进制模式下载（关键：.ts是二进制文件）
            response = requests.get(ts_url, headers=headers, timeout=15, stream=True)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024*1024):  # 1MB分块下载
                        if chunk:
                            f.write(chunk)
                print(f"成功下载：{os.path.basename(save_path)}")
                return True
            else:
                print(f"下载失败，状态码：{response.status_code}，重试第{i+1}次")
        except RequestException as e:
            print(f"网络错误：{str(e)}，重试第{i+1}次")
            time.sleep(3)  # 错误后延迟3秒再重试
    print(f"多次重试失败，放弃下载：{ts_url}")
    return False

# 3. 遍历下载所有.ts
for idx, ts_url in enumerate(ts_urls):
    # 按顺序命名.ts文件（避免合并时顺序错乱）
    ts_filename = f"ts_{idx+1:03d}.ts"  # 格式：ts_001.ts、ts_002.ts...
    save_path = os.path.join(save_dir, ts_filename)
    download_ts(ts_url, save_path)