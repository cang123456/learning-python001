
import random
import string
import requests
import lxml.etree,os



def get_pid_name(i): # 处理第i页 返回pid 和 name
    if i == 1:
        url = 'https://pic.netbian.com/'
    else:
        url = f'https://pic.netbian.com/index_{i}.html'

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    response = requests.get(url=url,headers=headers)
    response.encoding = 'gbk'

    html = lxml.etree.HTML(response.text)
    # // *[ @ id = "main"] / div[3] / ul / li[1] / a / img
    pid_list = html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@src') if html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@src') \
        else html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/img@src')
    name_list = html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@alt') if html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@alt') \
        else html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/img/@alt')

    pid_name = []
    for pid, name in zip(pid_list, name_list):
        pid1 = pid.split('/')[-1].split('-')[0]
        name1 = name + '.jpg'
        pid_name.append((pid1,name1))
        print(f"【日志】提取到 {pid1} ==== {name1}")

    return pid_name




def get_1_to2(pid_name):  # 1-》token -> url2
    url2 = []

    for pid, name in pid_name:
        # 核心：自动生成t参数（0-1之间的随机浮点数）
        t_param = random.random()  # 生成如0.xxxxxx的随机数
        t_param = f"{t_param:.{17}f}"
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
        response = requests.get(url,headers=headers)
        token =  response.text.split('=')[-1].split('"')[0]


        url = f"https://pic.netbian.com/e/extend/downpic.php?token={token}"

        rndzw = ''.join(random.choices(string.digits+string.ascii_lowercase+string.ascii_uppercase,k=20))
        print(f"rnd生成成功 \n{rndzw}")
        headers = {
            # 注意：HTTP/2的伪头字段(:authority/:method/:path/:scheme)无需放入headers，requests会自动处理
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

        response = requests.get(url,headers=headers)

        print(response.status_code)

        # print("内容",response.text)

        file_ = open(f"images/{name}.png",'wb')
        file_.write(response.content)
        file_.close()
        print('write success',f"images/{name}.png")


if __name__ == '__main__':
    i = 1
    while True:
        pid_name = get_pid_name(i)
        i += 1
        get_1_to2(pid_name)
