# 原始的Cookie字符串
cookie_str = 'PHPSESSID=7paf52pbg860udhvh2t4iroo60; RcGFvmlusername=qq_Gin484; RcGFvmluserid=8191109; RcGFvmlgroupid=1; RcGFvmlrnd=oTQfh7aTnNzUnIf7tWG0; RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQRQQJwrCOyl6ibiaQOZFWA0OAy2CRKiaI6RRMN7Ie75L04lCNSEeZXersOTicCmSQpuEKTYYtoiaA2vd15ia7HDIyVicwZiaQIDA5tYicXqlPts3REYHfiathUAU%5C%2F100%22%2C%220%22%2C%22qq_Gin484%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D; RcGFvmlauth=bcef2c523a4ec01c0108b67084952577'

# 初始化空字典存储解析后的Cookie
cookie_dict = {}

# 1. 按分号+空格拆分每个Cookie项
cookie_items = cookie_str.split('; ')

# 2. 遍历每个项，拆分键和值并存入字典
for item in cookie_items:
    # 使用split('=', 1)：只拆分第一个等号，避免值中包含等号导致错误
    key, value = item.split('=', 1)
    cookie_dict[key] = value

# 打印结果验证
print("解析后的Cookie字典：")
for key, value in cookie_dict.items():
    print(f"'{key}': '{value}',")


'''

PHPSESSID:7paf52pbg860udhvh2t4iroo60,
RcGFvmlusername=qq_Gin484,
RcGFvmluserid=8191109,
RcGFvmlgroupid=1,
RcGFvmlrnd=oTQfh7aTnNzUnIf7tWG0,
RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqapp%5C%2FAQRQQJwrCOyl6ibiaQOZFWA0OAy2CRKiaI6RRMN7Ie75L04lCNSEeZXersOTicCmSQpuEKTYYtoiaA2vd15ia7HDIyVicwZiaQIDA5tYicXqlPts3REYHfiathUAU%5C%2F100%22%2C%220%22%2C%22qq_Gin484%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D,
RcGFvmlauth=bcef2c523a4ec01c0108b67084952577
'''