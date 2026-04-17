import requests
import json

def get_ip_location(ip):
    # 替换为可用的公开IP查询接口
    url = f"http://ip-api.com/json/{ip}?lang=zh-CN"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 捕获HTTP请求错误
        data = json.loads(response.text)
        if data.get("status") != "success":
            return "查询失败：" + data.get("message", "未知错误")
        # 提取信息
        return {
            "国家": data["country"],
            "地区": data["regionName"],
            "城市": data["city"],
            "运营商": data["isp"]
        }
    except requests.exceptions.RequestException as e:
        return f"请求失败：{str(e)}"
    except json.JSONDecodeError:
        return "数据解析失败"

# 测试示例
print(get_ip_location(input()))