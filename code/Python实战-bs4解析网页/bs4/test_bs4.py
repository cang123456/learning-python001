from bs4 import BeautifulSoup

# 简单测试BeautifulSoup是否可以正常使用
html = "<html><body><p>测试内容</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.p.text)  # 应该输出: 测试内容