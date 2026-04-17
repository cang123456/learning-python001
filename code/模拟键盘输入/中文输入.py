import pyautogui
import time
import pyperclip  # 需要使用剪贴板


# 安装 pyperclip
# pip install pyperclip

def write_chinese(text, interval=0.05):
    """
    使用剪贴板输入中文
    这种方法更可靠
    """
    # 复制文本到剪贴板
    pyperclip.copy(text)

    # 粘贴内容
    pyautogui.hotkey('ctrl', 'v')  # 粘贴

    # 等待粘贴完成
    time.sleep(interval * len(text))


time.sleep(3)

content = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            content.append(line)

print(f"列表长度：{len(content)}")
print(f"内容：{content}")

for con in content:
    print(f"正在发送：{con}")

    # 使用剪贴板方法发送中文
    write_chinese(con, interval=0.05)

    # 发送消息（按回车）
    pyautogui.press('enter')

    # 等待一下
    time.sleep(0.5)

print("发送完成！")