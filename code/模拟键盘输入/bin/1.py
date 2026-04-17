import pyautogui
import time
import pyperclip

def write_chinese(text, interval=0.05):
    """
    使用剪贴板输入中文
    这种方法更可靠
    """
    # 复制文本到剪贴板
    pyperclip.copy(text)

    # 粘贴内容
    pyautogui.hotkey('ctrl', 'v')

time.sleep(3)

content = []

with open('input.txt','r',encoding='utf-8') as f:
    for line in f:
        # print(line)
        line = line.strip()
        if line:
            content.append(line)
print(content)
print("列表长度：" + str(len(content)))



for con in content:
    # pyautogui.typewrite(con)
    # pyautogui.press('enter')
    conlen = len(con)
    lennow = 0
    while(lennow < conlen):
        print("lennow:" + str(lennow))
        lend = min(lennow+30, conlen)
        print("conlen:" + str(lend))
        s1 = con[lennow:lend]
        s2 = s1.rstrip('\n\r ')
        if s2:  # 只有当s2非空时才输入
            write_chinese(s2)
            pyautogui.press('down')
        # pyautogui.write(con[lennow:lend], interval=0.05)
        print(repr(con[lennow:lend]))  # 使用repr显示特殊字符
        time.sleep(0.1)  # 等待输入完成

        lennow = lennow + 30

