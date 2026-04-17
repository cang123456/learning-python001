import random
import string
import requests
import lxml.etree
import os

# 新增：创建Session自动维护Cookie，替代硬编码Cookie
session = requests.Session()


def get_pid_name(i):  # 处理第i页 返回pid 和 name
    if i == 1:
        url = 'https://pic.netbian.com/'
    else:
        url = f'https://pic.netbian.com/index_{i}.html'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    # 改动1：改用session请求，自动维护Cookie
    response = session.get(url=url, headers=headers, timeout=10)
    response.encoding = 'gbk'

    html = lxml.etree.HTML(response.text)
    # 改动2：修复XPath语法错误（a/img@src → a/img/@src）
    pid_list = html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@src') if html.xpath(
        '//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@src') \
        else html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/img/@src')  # 修复这里的/
    name_list = html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@alt') if html.xpath(
        '//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@alt') \
        else html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/img/@alt')

    pid_name = []
    # 新增：同时保存原图地址（用于Token失效时备用）
    src_list = pid_list.copy()
    for pid, name, src in zip(pid_list, name_list, src_list):
        pid1 = pid.split('/')[-1].split('-')[0]
        name1 = name + '.jpg'
        # 改动：把src也加入返回值（备用下载地址）
        pid_name.append((pid1, name1, src))
        print(f"【日志】提取到 {pid1} ==== {name1}")

    return pid_name


# 新增：备用下载函数（Token失效时调用）
def download_by_src(src, name):
    try:
        # 从缩略图地址推导原图地址
        if '_' in src:
            origin_src = src.rsplit('_', 1)[0] + '.jpg'
        else:
            origin_src = src
        origin_url = 'https://pic.netbian.com' + origin_src
        # 请求原图
        response = session.get(origin_url, timeout=10)
        if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
            # 创建images目录
            if not os.path.exists('images'):
                os.makedirs('images')
            # 改动3：修复文件后缀重复问题（去掉.png）
            file_ = open(f"images/{name}", 'wb')
            file_.write(response.content)
            file_.close()
            print(f"【备用方案成功】下载 {name} (通过原图地址)")
            return True
        else:
            print(f"【备用方案失败】{name} 原图地址无效")
            return False
    except Exception as e:
        print(f"【备用方案异常】{name}：{str(e)}")
        return False


def get_1_to2(pid_name):  # 1-》token -> url2
    for pid, name, src in pid_name:  # 新增：接收src参数
        # 核心：自动生成t参数（0-1之间的随机浮点数）
        t_param = random.random()  # 生成如0.xxxxxx的随机数
        t_param = f"{t_param:.{16}f}"
        rndzw = ''.join(random.choices(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=20))
        # 构造URL（替换id和t参数）
        url = f"https://pic.netbian.com/e/extend/downpic.php?id={pid}&t={t_param}"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cookie": f"PHPSESSID=lakvbpqrrefglcbbb1aotvqug6; RcGFvmlusername=qq_Gin484; RcGFvmluserid=8191109; RcGFvmlgroupid=1; RcGFvmlrnd=o{rndzw}; RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQRQQJwrCOyl6ibiaQOZFWA0OAy2CRKiaI6RRMN7Ie75L04lCNSEeZXersOTicCmSQpuEKTYYtoiaA2vd15ia7HDIyVicwZiaQIDA5tYicXqlPts3REYHfiathUAU%5C%2F100%22%2C%220%22%2C%22qq_Gin484%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D; RcGFvmlauth=3ff1174dc39ee4f1e6a920a87a4938aa",
            "Priority": "u=1, i",
            "Referer": f"https://pic.netbian.com/tupian/{pid}.html",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
            "X-Requested-With": "XMLHttpRequest"  # AJAX请求标识，需保留
        }
        try:
            response = session.get(url, headers=headers, timeout=10)
            response.encoding = 'gbk'
            # 改动5：判断Token接口是否返回无效值
            if response.text.strip() == '{"msg":0}':
                print(f"【警告】PID {pid} Token失效，切换备用方案下载")
                # 调用备用下载函数
                download_by_src(src, name)
                continue

            token = response.text.split('=')[-1].split('"')[0]
            if not token:
                print(f"【警告】PID {pid} Token为空，切换备用方案")
                download_by_src(src, name)
                continue

            url = f"https://pic.netbian.com/e/extend/downpic.php?token={token}"
            rndzw = ''.join(random.choices(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=20))
            print(f"rnd生成成功 \n{rndzw}")
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cookie": f"PHPSESSID=lakvbpqrrefglcbbb1aotvqug6; RcGFvmlusername=qq_Gin484; RcGFvmluserid=8191109; RcGFvmlgroupid=1; RcGFvmlrnd={rndzw}; RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQRQQJwrCOyl6ibiaQOZFWA0OAy2CRKiaI6RRMN7Ie75L04lCNSEeZXersOTicCmSQpuEKTYYtoiaA2vd15ia7HDIyVicwZiaQIDA5tYicXqlPts3REYHfiathUAU%5C%2F100%22%2C%220%22%2C%22qq_Gin484%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D; RcGFvmlauth=3ff1174dc39ee4f1e6a920a87a4938aa",
                "Priority": "u=0, i",
                "Referer": f"https://pic.netbian.com/tupian/{pid}.html",
                "sec-ch-ua": "\"Microsoft Edge\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "iframe",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
            }

            response = session.get(url, headers=headers, timeout=10)
            print(f"【日志】PID {pid} 响应状态码：{response.status_code}")

            # 改动7：修复文件命名重复后缀（去掉.png）
            if not os.path.exists('images'):
                os.makedirs('images')
            file_ = open(f"images/{name}", 'wb')  # 原name已经是xxx.jpg，无需再加.png
            file_.write(response.content)
            file_.close()
            print('write success', f"images/{name}")
        except Exception as e:
            print(f"【错误】PID {pid} 下载失败：{str(e)}，尝试备用方案")
            download_by_src(src, name)


if __name__ == '__main__':
    i = 1
    # 改动8：增加页数限制，避免无限循环（可根据需要调整）
    max_page = 20
    while i <= max_page:
        pid_name = get_pid_name(i)
        if not pid_name:  # 无数据时停止
            break
        i += 1
        get_1_to2(pid_name)