import csv
import os
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot

from DrissionPage import ChromiumPage
import wordcloud

import re

import db_connect as db




page = ChromiumPage() # 1 cj

page.listen.start('comment/list') # 关键字 这个用的是关键字 同时抖音路径一直变化

# 打开这个作者主页 打开对应视频

# url = 'https://www.douyin.com/user/MS4wLjABAAAA4WPFzQuJ252MaVOzivfv03loTmtvC7we8toH2rhR5ZQ?from_tab_name=main&modal_id=7576532775872761124&showTab=post&vid=7573343075754429738'
url = 'https://www.douyin.com/user/MS4wLjABAAAAybf5fIC1JRCQdwO5XSPSv5PEaVlnDXHRiaQYRz0prXMeOgYz1LGsqa2pvAvYhVoL?from_tab_name=main&modal_id=7569571011752413681&vid=7581808247540026661'
page.get(url)

# 点击评论botton == 看见评论
ele1 = page.ele('css:.jp8u3iov')
ele1.click()

text1 = ''

def write_csv(row):
    csv_headers = ["用户昵称", "IP属地", "评论文本", "用户主页链接"]
    # 3. 判断文件是否存在，决定是否写入表头
    file_exists = os.path.exists('douyin_pinlun.csv')
    with open('douyin_pinlun.csv','a',encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(csv_headers)
        writer.writerow(row)


while True:
    result = page.listen.wait() # 等 结果

    JSON = result.response.body

    comment_list = JSON['comments']

    for comment in comment_list:
        name = comment['user']['nickname']
        ip = comment['ip_label']
        text = comment['text']
        text1 += text
        user_url = 'https://www.douyin.com/user/' + comment['user']['sec_uid']
        print(f"用户名为：{name} ip{ip} ：【{text}】 个人主页{user_url}")

        # row = [name,ip,text,user_url]
        # write_csv(row)
        row = (name,ip,text,user_url)
        db.solve(row)


    try:
        # 取完数据 滑动一次
        ele2 = page.ele('加载中')
        page.scroll.to_see('css:.ETuXBjRi')
    except Exception as e:
        print('='*100,e)

####################################词云生成模块
# with open('command.txt','w',encoding='utf-8') as f:
#     f.write(text1)
#
# with open('command.txt','r',encoding='utf-8') as f:
#     text1 = re.sub(f'[.*?]','', text1)
#
#
#
# wc = wordcloud.WordCloud(
#     font_path='11.TTF',
#     width=1920, height=1080,
#     background_color='white'
# ).generate(text1)
#
#
# matplotlib.pyplot.imshow(wc) # 显示词云
# matplotlib.pyplot.show()
####################################词云生成模块

