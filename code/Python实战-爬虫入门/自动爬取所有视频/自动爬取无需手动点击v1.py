import os
import time
import random
import requests
import m3u8
from requests.exceptions import RequestException
from concurrent.futures import ThreadPoolExecutor, as_completed









# 获取链接






# ===================== 核心配置（根据需要调整）=====================
# 1. 目标m3u8链接（替换为你抓取到的实际链接）
sb = ''
while 1:
    sb = input()
    if sb:
        break

M3U8_URL = sb
# 2. 下载保存目录（避免中文/空格路径）
SAVE_DIR = r"D:\Webcrawlers\test"
# 3. 多线程配置（关键：线程数建议3-5，过高易被封）
MAX_THREADS = 100
# 4. 请求头（需和浏览器一致，从开发者工具复制）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://vip.dytt-cinema.com/",  # 视频播放页URL
    # "Cookie": ""  # 登录后的Cookie（可选，若需要权限）
}
# 5. 反爬配置
RETRY_TIMES = 3  # 单个文件重试次数
DELAY_RANGE = (0.2, 0.5)  # 每次请求随机延迟（秒）


# ===================== 工具函数 =====================
def parse_m3u8():
    """解析m3u8文件，提取所有.ts切片的完整URL"""
    try:
        response = requests.get(M3U8_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()  # 非200状态码抛出异常
        m3u8_obj = m3u8.loads(response.text)
        ts_urls = []
        for segment in m3u8_obj.segments:
            # 处理相对路径，拼接完整URL
            ts_uri = segment.uri
            if not ts_uri.startswith("http"):
                ts_uri = M3U8_URL.rsplit("/", 1)[0] + "/" + ts_uri
            ts_urls.append(ts_uri)
        print(f"✅ 成功解析m3u8，共找到 {len(ts_urls)} 个.ts切片")
        return ts_urls
    except Exception as e:
        print(f"❌ 解析m3u8失败：{str(e)}")
        return []


def download_ts(ts_url, save_path):
    """单个.ts文件下载函数（带重试+延迟+二进制下载）"""
    # 随机延迟，模拟人工请求（反爬关键）
    time.sleep(random.uniform(*DELAY_RANGE))

    for retry in range(RETRY_TIMES):
        try:
            response = requests.get(
                ts_url,
                headers=HEADERS,
                timeout=15,
                stream=True,  # 分块下载，避免内存溢出
                verify=False  # 忽略SSL证书错误（部分站点需要）
            )
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):  # 1MB分块
                        if chunk:
                            f.write(chunk)
                return (True, f"成功：{os.path.basename(save_path)}")
            else:
                err_msg = f"状态码{response.status_code}，重试第{retry + 1}次"
                if retry == RETRY_TIMES - 1:
                    return (False, f"失败：{os.path.basename(save_path)} - {err_msg}")
                time.sleep(3)  # 失败后延迟3秒重试
        except RequestException as e:
            err_msg = f"网络错误：{str(e)}，重试第{retry + 1}次"
            if retry == RETRY_TIMES - 1:
                return (False, f"失败：{os.path.basename(save_path)} - {err_msg}")
            time.sleep(3)


# ===================== 主函数（多线程执行）=====================
def main():
    # 1. 创建保存目录
    os.makedirs(SAVE_DIR, exist_ok=True)

    # 2. 解析m3u8，获取ts切片URL列表
    ts_urls = parse_m3u8()
    if not ts_urls:
        print("❌ 无可用的.ts切片URL，程序退出")
        return

    # 3. 初始化线程池（控制最大并发数）
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # 存储任务：key=任务对象，value=文件名
        task_dict = {}
        for idx, ts_url in enumerate(ts_urls):
            # 按顺序命名（保证合并时不打乱）：ts_001.ts、ts_002.ts...
            ts_filename = f"ts_{idx + 1:03d}.ts"
            save_path = os.path.join(SAVE_DIR, ts_filename)
            # 提交下载任务到线程池
            task = executor.submit(download_ts, ts_url, save_path)
            task_dict[task] = ts_filename

        # 4. 遍历任务结果，输出进度
        success_count = 0
        fail_count = 0
        for task in as_completed(task_dict):
            filename = task_dict[task]
            try:
                is_success, msg = task.result()
                if is_success:
                    success_count += 1
                else:
                    fail_count += 1
                print(msg)
            except Exception as e:
                fail_count += 1
                print(f"❌ 任务异常：{filename} - {str(e)}")

        # 5. 输出最终统计
        print("\n" + "=" * 50)
        print(f"📊 下载完成：成功 {success_count} 个，失败 {fail_count} 个")
        print(f"📁 保存路径：{SAVE_DIR}")
        print("💡 失败文件可重新运行程序补下（已下载的文件不会重复下载）")


if __name__ == "__main__":
    # 忽略requests的SSL警告（可选）
    requests.packages.urllib3.disable_warnings()
    main()
    os.system("cd D:/Webcrawlers & start D:/Webcrawlers/fix.exe")