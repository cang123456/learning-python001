import random
import string
import requests
import lxml.etree,os




url = 'https://pic.netbian.com/'


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}



response = requests.get(url=url,headers=headers)
response.encoding = 'gbk'

# print(f"【日志】当前页面请求状态码：{response.status_code}")


html = lxml.etree.HTML(response.text)

# data = html.xpth("weizhi")
# print("【日志】进入页面 获取 pidlist 和 名称lsit....")
pid_list = html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@src')
name_list = html.xpath('//*[@id="main"]/div[3]/ul/li[*]/a/span/img/@alt')

print("【日志】开始解析单个pid 和 name 存储到元祖中....")
pid_name = []
for pid, name in zip(pid_list,name_list):
    pid1 = pid.split('/')[-1].split('-')[0]
    name1 = name + '.jpg'
    pid_name.append({pid1:name1})
    print(f"【日志】提取到 {pid1} ==== {name1}")
    if os.path.exists(f"d:\\images\\{name1}"):
        print(f"【日志】图片{name1}已经存在，继续下一个....")
        continue
    url1 = f'https://pic.netbian.com/e/extend/downpic.php?id={pid1}&t=0.8276906904130226'

    rndzw = ''.join(random.choices(string.digits+string.ascii_lowercase+string.ascii_uppercase,k=20))
    print(f"【日志】cookie中的rnd生成成功 \n{rndzw}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": f"https://pic.netbian.com/tupian/{pid1}.html",
        "Connection": "keep-alive"
    }

    # cookie = {
    #     'PHPSESSID': 'g9L3h4L3uf3n0b9giabdems0r7',
    #     'RcGFvmLusername': '%CE%A2%B2%A9%D6%AA%C3%FB',
    #     'RcGFvmLuserid': '8117025',
    #     'RcGFvmLgroupid': '1',
    #     'RcGFvmLrnd': f'{rndzw}',
    #     'RcGFvmLinfo': '%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQsia1pgCMCLjLh5Wns56w15LA0SDLPeB4KKTYc12dj7R1RASm9X3d0dJD50J9FfdiaXnbLsgj%5C%2F100%22%20%220%22%20%22%5Cu5fae%5Cu535a%5Cu77e5%5Cu540d%22%20%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D',
    #     'RcGFvmLauth': '0d4915ad4579818bbac3a3d012af6d79'
    # }

    # cookie = {
    #     'PHPSESSID': '7paf52pbg860udhvh2t4iroo60',
    #     'RcGFvmlusername': 'qq_Gin484',
    #     'RcGFvmluserid': '8191109',
    #     'RcGFvmlgroupid': '1',
    #     'RcGFvmlrnd': f'{rndzw}',
    #     'RcGFvmlinfo': '%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQRQQJwrCOyl6ibiaQOZFWA0OAy2CRKiaI6RRMN7Ie75L04lCNSEeZXersOTicCmSQpuEKTYYtoiaA2vd15ia7HDIyVicwZiaQIDA5tYicXqlPts3REYHfiathUAU%5C%2F100%22%2C%220%22%2C%22qq_Gin484%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D',
    #     'RcGFvmlauth': 'bcef2c523a4ec01c0108b67084952577'
    # }

    cookie = {
        "PHPSESSID":"lakvbpqrrefglcbbb1aotvqug6",
        "RcGFvmlusername":"qq_Gin484",
        "RcGFvmluserid":"8191109",
        "RcGFvmlgroupid":"1",
        "RcGFvmlrnd":f"{rndzw}", #oyneODT9wR2Ytm3ihbXK
        "RcGFvmlinfo":"%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQRQQJwrCOyl6ibiaQOZFWA0OAy2CRKiaI6RRMN7Ie75L04lCNSEeZXersOTicCmSQpuEKTYYtoiaA2vd15ia7HDIyVicwZiaQIDA5tYicXqlPts3REYHfiathUAU%5C%2F100%22%2C%220%22%2C%22qq_Gin484%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D",
        "RcGFvmlauth":"3ff1174dc39ee4f1e6a920a87a4938aa",

    }

    response1 = requests.get(url=url1,headers=headers,cookies=cookie)
    print(f"【日志】第一次请求结果:{response1.status_code}{' '*5}{response1.text}")

    token = response1.text.split('=')[-1].split('"')[0]
    print(f"【日志】拆分token完成{token}")

    url2 = f"https://pic.netbian.com/e/extend/downpic.php?token={token}"

    # response2 = requests.get(url2, headers=headers)
    # print(f"【日志】请求第二个链接{response2.status_code}")
    # print(f"【日志】请求第二个链接的内容text：{response2.text}")
    # # print(response2.text)
    #
    #
    # # open(f'images/{name1}','wb').write(response2.content)
    #
    # with open(f"d:\\images\\{name1}", 'wb') as f:
    #     print("【日志】图片大小为空！",len(response2.content))
    #     if len(response2.content) > 0:
    #         f.write(response2.content)
    #     else:
    #         print(f"【日志】图片: {name1} 大小为空！")
    # print(f"【日志】保存图片:{name1} \n\n")
    #
    #
    #



