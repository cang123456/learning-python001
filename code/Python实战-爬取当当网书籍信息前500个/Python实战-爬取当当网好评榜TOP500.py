import random
import time

import requests
import json
import re

# 通用Chrome浏览器请求头（推荐优先用）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# url = 'http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-recent30-0-0-1-'

# request_dandan('http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1')

# request
def request_dandan():
    for page in range(1,26):
        url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-all-0-0-1-' + str(page)
        # print(url)
        try:
            response = requests.get(url,headers=headers,timeout=5)
            # print(f"requset 成功{page}")
            write_info(response.text)
            # print(f"写入成功{page}")
            time.sleep(random.uniform(0.3,0.9))
        except Exception as e:
            print(e)
        time.sleep(random.uniform(0.3,0.8))

def solve(items):
    # 错误1：字典{}不能存多个对象，改成列表[]（列表才有append方法）
    answer = []
    for item in items:
        answer.append({
            'range':item[0],
            'imgurl':item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price':item[6]
        })  # 补全闭合括号
    return answer



def write_info(html:str):
    print("start write_info")
    # 改用第一个代码的高效正则（删掉硬编码+匹配title+price_n）
    patten0 = r'<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>'
    try:
        patten = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
        items = re.findall(patten,html)
        book_items = solve(items)
        for book_item in book_items:
            print("start wirte =========>  " + str(book_item))
            with open("answer.txt",'a',encoding='utf-8') as f:
                f.write(json.dumps(book_item,ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"re错误{e}")
    # print("end write_info")




request_dandan()