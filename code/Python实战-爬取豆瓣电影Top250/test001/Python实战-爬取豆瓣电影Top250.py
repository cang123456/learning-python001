import requests
from bs4 import BeautifulSoup
import xlwt as xl


# 请求 解析 存储



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


def request_douban(page):
    url = 'https://movie.douban.com/top250?start=' + str(page*25) + '&filter='
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        print(f"【日志】第{page+1}页请求成功")
        print(response.text)
    soup = BeautifulSoup(response.text,'lxml')

    write_excel(soup)


book = xl.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
sheet.write(0,0,'名称')
sheet.write(0,1,'图片链接')
sheet.write(0,2,'排名')
sheet.write(0,3,'评分')
sheet.write(0,4,'作者')
sheet.write(0,5,'简介')


def write_excel(soup):
    lst = soup.find(class_='grid_view').find_all('li')
    for item in lst:
        itemname = item.find(class_='title').string
        itemimg = item.find('img').get('src')
        itemindex = item.find(class_="").string
        itemsocre = item.find(class_='rating_num')
        itemauthor = item.find('p').text
        iteminq = item.find(class_='inq').string
        print(f'''【日志】soup解析内容:itemname = {item.find(class_='title').string},        itemimg = {item.find('img').get('src')},       itemindex = {item.find(class_="").string},        itemsocre = {item.find(class_='')},     itemauthor = {item.find('p').text},        iteminq = {item.find(class_='inq').string}''')

    # lst = soup.find(class_='grid_view').find_all('li')
    # for item in lst:
    #     i_name = item.find(class_='title').string



if __name__ == '__main__':
    for i in range(0,25):
        request_douban(i)










