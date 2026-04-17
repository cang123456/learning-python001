# 问题1：缺少必要导入 → 补充（新手易漏）
import requests
import json
import re

# 问题2：添加请求头（避免被服务器识别为爬虫）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # 问题3：多余的f.close() → 删除（with语句自动关闭文件）
        # f.close()

def parse_result(html):
    # 问题4：正则保留你的高效写法，仅确保语法正确
    pattern = re.compile(
        r'<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            # 问题5：拼写错误 iamge → image（新手易写错）
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def request_dandan(url):
    try:
        # 问题6：请求时添加headers+超时 → 避免卡住/被拦截
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            # 问题7：设置编码为gbk → 解决当当网HTML乱码（核心！）
            response.encoding = 'gbk'
            return response.text
    except requests.RequestException as e:
        # 问题8：添加错误提示 → 新手知道哪里错了
        print(f"请求失败：{e}")
        return None

# 问题9：重复定义main函数 → 删除多余的第二个main，修正第一个main的逻辑
def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    print(f"正在爬取第{page}页：{url}")
    html = request_dandan(url)
    # 问题10：判断html不为空再解析 → 避免None传入正则报错
    if html:
        items = parse_result(html)
        for item in items:
            write_item_to_file(item)

if __name__ == "__main__":
    # 循环爬取1-25页
    for i in range(1, 26):
        main(i)