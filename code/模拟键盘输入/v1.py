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

# https://github.com/cang123456/Project-backup.git

content = []

with open('input.txt','r',encoding='utf-8') as f:
    for line in f:
        # print(line)
        line = line.strip()
        if line:
            content.append(line)
print(content)
print("列表长度：" + str(len(content)))

f1 = 'n'



def run():
    print("3秒后运行！")
    time.sleep(3)
    for con in content:
        # pyautogui.typewrite(con)
        # pyautogui.press('enter')
        conlen = len(con)
        lennow = 0
        while(lennow < conlen):
            flag = 0
            if lennow == 0:
                pyautogui.press('space')
                pyautogui.press('space')
                flag = 2
            print("lennow:" + str(lennow))
            if flag == 0:# 正常输入
                lend = min(lennow+30, conlen)
            else:# 首行输入
                lend = min(lennow+28, conlen)
            print("conlen:" + str(lend))
            s1 = con[lennow:lend]
            s2 = s1.rstrip('\n\r')
            write_chinese(s2)
            # pyautogui.write(con[lennow:lend], interval=0.05)
            print(con[lennow:lend])
            time.sleep(0.06)  # 等待输入完成
            pyautogui.press('down')
            lennow = lennow + 30 - flag

f1 = input("继续y/n：")

if(f1 == 'y'):
    run()
