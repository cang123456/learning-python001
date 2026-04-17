import time

import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import db_connect as db

# 复制的xpath
# //*[@id="content"]/div/div[1]/ol/li[*]


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0'
}
for i in range(0,25):
    time.sleep(1)
    url = f'https://movie.douban.com/top250?start={i*25}&filter='

    response = requests.get(url=url,headers=headers)

    html = etree.HTML(response.text)

    li_list = html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]')

    for li in li_list:
        name = li.xpath('.//span[@class="title"]/text()')[0]
        imgurl = li.xpath('.//img/@src')[0]
        paimin = li.xpath('.//em/text()')[0]
        pinfen = li.xpath('.//span[@class="rating_num"]/text()')[0]
        author = re.sub('[\xa0;\n\t ]','',li.xpath('.//div[@class="bd"]/p/text()')[0])
        numofeva = li.xpath('.//div[@class="bd"]/div/span[4]/text()')[0]
        mv_lab = re.sub('[\xa0;\n\t ]','',(li.xpath('.//p[@class="quote"]/span/text()')[0] if li.xpath('.//p[@class="quote"]/span/text()') else "")+li.xpath('.//div[@class="bd"]/p/text()')[1] if len(li.xpath('.//div[@class="bd"]/p/text()')) >= 2 else "")
        aws = (name,imgurl,int(paimin),pinfen,author,numofeva,mv_lab)
        db.solve(aws)
        print('【日志】正在写入：',name,imgurl,paimin,pinfen,author,numofeva,mv_lab)



















