import time

import requests
from bs4 import BeautifulSoup
import csv, random


url = "https://movie.douban.com/top250"
# 发送request get请求时候，记得加上请求头headers+User-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://movie.douban.com/"
}

data = []

def solve(soup_list):
    for sp in soup_list:
        # 获取电影名称
        title = sp.find("span",class_="title").text  # print(sp.find("span",class_="title")) 返回的是类似<span class="title">肖申克的救赎</span>，这样不行

        # # 获取电影评分
        score = sp.find("span", class_="rating_num").text

        # # 获取电影评价人数
        dadivlst = sp.find_all("div")  # dadiv = soup.find_all("div",class='')       这个是寻找div 且 class为空的
        dadiv = dadivlst[len(dadivlst) - 1]

        pjspanlst = dadiv.find_all("span")
        pjspan = pjspanlst[len(pjspanlst) - 1]

        # # 获取电影信息
        infodiv = sp.find("div", class_="bd")
        infop = infodiv.find("p")
        quote = infop.text

        data.append({"电影名": title, "评分": score,  "评价人数": pjspan.text,"简介": quote})
        # 保存数据为 csv/excel

for i in range(0,250,25):
    # https://movie.douban.com/top250?start=0&filter=
    url_new = url + "?start=" + str(i) + "&filter="
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    soup_list = soup.find_all("div", class_="item")
    solve(soup_list)
    time.sleep(random.uniform(1,3))

# 发送get请求
# response = requests.get(url,headers=headers)

# 查看请求是否成功
# if response.status_code == 200:
#     html = response.text
#     print("200 请求成功")
# else:
#     print(f"请求失败{response.status_code}")



# 核心提取环节： 用BeautifulSoup解析html，通过标签+id定位数据
# soup = BeautifulSoup(html,"lxml")

# print(html)
# print("="*80)
# print(soup)

    # li li li li.... 结构 li->div class=itme li li li li li
# soup_list = soup.find_all("div",class_="item")

with open("douban.csv","a+",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["电影名", "评分","评价人数", "简介"])
    for item in data:
        writer.writerow([item["电影名"], item["评分"], item["评价人数"], item["简介"]])


with open("douban.txt","a+",encoding="utf-8") as f:
    s1 = f"{"电影名":<10}{"评分":<5}{"评价人数":<12}{"简介"}"
    f.write(s1 + '\n')
    for item in data:
        s2 = f"{item['电影名']:<10}{item['评分']:<5}{item['评价人数']:<12}{item['简介']}"
        f.write(s2 + '\n')




'''
<div class="item">
                <div class="pic">
                    <em>1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292052/">
                            <span class="title">肖申克的救赎</span>
                                    <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                                <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p>
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>

                        
                        <div>
                            <span class="rating5-t"></span>
                            <span class="rating_num" property="v:average">9.7</span>
                            <span property="v:best" content="10.0"></span>
                            <span>3244298人评价</span>
                        </div>

                            <p class="quote">
                                <span>希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
'''










