import requests
from bs4 import BeautifulSoup
import xlwt
import time  # 用于添加请求延迟，避免反爬

# 请求头，模拟浏览器访问
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://movie.douban.com/"
}

# 初始化Excel工作簿和工作表（全局变量，方便多页写入）
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
# 设置Excel表头
headers = ['排名', '电影名称', '海报链接', '评分', '导演/演员信息', '引言']
for col, header in enumerate(headers):
    worksheet.write(0, col, header)
# 记录Excel的行号（从第2行开始写入数据，第1行是表头）
excel_row = 1


def save_to_excel(soup):
    """解析网页数据并写入Excel"""
    global excel_row  # 使用全局行号变量
    try:
        lst = soup.find(class_='grid_view')
        if not lst:
            print("未找到grid_view容器，跳过当前页")
            return
        list_items = lst.find_all('li')

        for item in list_items:
            # 1. 提取排名（修复空class问题：豆瓣排名在class='pic'下的em标签）
            index_elem = item.find(class_='pic').find('em') if item.find(class_='pic') else None
            item_index = index_elem.string if index_elem else "无排名"

            # 2. 提取电影名称（处理元素缺失）
            name_elem = item.find(class_='title')
            item_name = name_elem.string if name_elem else "无名称"

            # 3. 提取海报链接（处理元素缺失）
            img_elem = item.find('a').find('img') if item.find('a') else None
            item_img = img_elem.get('src') if img_elem else "无链接"

            # 4. 提取评分（处理元素缺失）
            score_elem = item.find(class_='rating_num')
            item_score = score_elem.string if score_elem else "无评分"

            # 5. 提取导演/演员信息（处理元素缺失，去除多余空格）
            author_elem = item.find('p')
            item_author = author_elem.text.strip().replace('\n', ' ').replace('  ', ' ') if author_elem else "无信息"

            # 6. 提取引言（处理元素缺失）
            intr_elem = item.find(class_='inq')
            item_intr = intr_elem.string if intr_elem else "无引言"

            # 打印爬取结果（简化版）
            print(f'爬取电影：{item_index} | {item_name} | {item_score} | {item_intr}')

            # 写入Excel（按列对应：排名、名称、海报、评分、导演信息、引言）
            worksheet.write(excel_row, 0, item_index)
            worksheet.write(excel_row, 1, item_name)
            worksheet.write(excel_row, 2, item_img)
            worksheet.write(excel_row, 3, item_score)
            worksheet.write(excel_row, 4, item_author)
            worksheet.write(excel_row, 5, item_intr)

            excel_row += 1  # 行号自增，准备写入下一条数据
    except Exception as e:
        print(f"解析/保存数据时出错：{str(e)}")


def request_douban(url):
    """发送请求，获取网页内容（增加异常处理）"""
    try:
        # 设置超时时间10秒，避免卡住
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"请求失败，状态码：{response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"请求异常：{str(e)}")
        return None


def main(page):
    """爬取指定页码的豆瓣Top250数据"""
    url = f'https://movie.douban.com/top250?start={page * 25}&filter='
    print(f"\n开始爬取第{page + 1}页数据...")
    html = request_douban(url)
    if html:  # 只有获取到有效html才解析
        soup = BeautifulSoup(html, 'lxml')
        save_to_excel(soup)
        # 添加1秒延迟，避免请求过快被反爬
        time.sleep(1)
    else:
        print(f"第{page + 1}页未获取到数据，跳过")


if __name__ == '__main__':
    # 豆瓣Top250共10页（250条），所以循环0-9即可（原代码21页超出范围）
    for i in range(0, 10):
        main(i)

    # 所有页爬取完成后，保存Excel文件
    workbook.save('豆瓣电影Top250.xls')
    print("\n所有数据爬取完成！文件已保存为：豆瓣电影Top250.xls")