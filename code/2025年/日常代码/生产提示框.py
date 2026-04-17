import time
import tkinter as tk
import random

# 温馨提示文本列表
tips = [
    "我想你了", "保持微笑呀", "梦想成真", "愿所有烦恼都消失",
    "每天都要元气满满", "多喝水哦~", "别熬夜", "天冷了，注意保暖",
    "期待下一次见面", "好好爱自己", "今天过得开心嘛", "早点休息"
]


# 生成随机颜色（RGB转十六进制）
def get_random_color():
    r = random.randint(150, 255)  # 避免颜色过深，文字看不清
    g = random.randint(150, 255)
    b = random.randint(150, 255)
    return f'#{r:02x}{g:02x}{b:02x}'


# 主函数：创建多个提示框并记录顺序
def create_tip_windows(root, num_windows=30, delay=3000):
    windows = []  # 记录窗口创建顺序
    for _ in range(num_windows):
        # 创建顶层窗口（Toplevel）
        top = tk.Toplevel(root)
        top.overrideredirect(False)
        top.attributes('-topmost', False)

        # 随机位置
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = random.randint(50, screen_width - 200)
        y = random.randint(50, screen_height - 100)
        top.geometry(f"200x100+{x}+{y}")

        # 随机背景色和提示文本
        bg_color = get_random_color()
        tip_text = random.choice(tips)

        # 显示文本
        label = tk.Label(
            top,
            text=tip_text,
            font=('微软雅黑', 12),
            bg=bg_color,
            width=20,
            height=5,
            justify='center'
        )
        label.pack(fill=tk.BOTH, expand=True)

        windows.append(top)# 记录窗口


    # 按顺序关闭窗口（每个间隔0.5秒）
    def close_windows(win_list, index=0):
        if index < len(win_list):
            win_list[index].destroy()  # 关闭当前窗口
            # 0.5秒后关闭下一个窗口
            root.after(1, close_windows, win_list, index + 1)
        else:
            root.destroy()  # 所有窗口关闭后，退出程序

    # 延迟指定时间后开始关闭（单位：毫秒，3000=3秒）
    root.after(delay, close_windows, windows)


# 初始化主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 创建提示框（3秒后开始按顺序关闭，每个间隔0.5秒）
create_tip_windows(root, num_windows=159, delay=3000)

root.mainloop()