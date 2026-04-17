import pyautogui
import time

# 读取1.txt文件内容
try:
    with open('1.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("错误：未找到1.txt文件，请确保文件存在于当前目录下")
    exit()
except Exception as e:
    print(f"读取文件时发生错误：{e}")
    exit()

# 等待几秒钟，让用户切换到需要输入的窗口（如记事本、文档等）
print("请在5秒内切换到输入窗口...")
time.sleep(5)

# 模拟键盘输入文本，处理换行符
lines = content.split('\n')
for i, line in enumerate(lines):
    # 使用更可靠的方式输入中文字符
    pyautogui.write(line, interval=0.1)
    if i < len(lines) - 1:  # 如果不是最后一行，按回车键
        pyautogui.press('enter')
print("输入完成")




'''
abasdlkfjklalksdfjl





'''