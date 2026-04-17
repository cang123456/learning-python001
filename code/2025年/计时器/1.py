import tkinter as tk
from tkinter import messagebox, ttk
import time
import winsound  # Windows 系统声音提醒（Mac/Linux 需替换，见备注）

class PopupTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("弹窗计时器")
        self.root.geometry("400x250")  # 窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小

        # 计时状态变量
        self.is_running = False  # 是否正在计时
        self.is_paused = False   # 是否暂停
        self.remaining_time = 0  # 剩余时间（秒）
        self.start_time = 0      # 开始计时的时间戳
        self.timer_id = None     # 定时器任务ID

        # 1. 输入框：设置计时时长（分钟）
        self.label = ttk.Label(root, text="计时时长（分钟）：", font=("Arial", 12))
        self.label.pack(pady=10)
#
        self.time_entry = ttk.Entry(root, font=("Arial", 12), width=20)
        self.time_entry.insert(0, "1")  # 默认1分钟
        self.time_entry.pack(pady=5)

        # 2. 倒计时显示标签
        self.countdown_label = ttk.Label(root, text="00:00:00", font=("Arial", 20, "bold"))
        self.countdown_label.pack(pady=15)

        # 3. 按钮区域
        self.btn_frame = ttk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.start_btn = ttk.Button(self.btn_frame, text="开始计时", command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = ttk.Button(self.btn_frame, text="暂停", command=self.pause_timer, state=tk.DISABLED)
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = ttk.Button(self.btn_frame, text="重置", command=self.reset_timer)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def format_time(self, seconds):
        """将秒数格式化为 时:分:秒 格式"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

    def start_timer(self):
        """开始计时"""
        # 校验输入的时长
        try:
            minutes = float(self.time_entry.get())
            if minutes <= 0:
                messagebox.showerror("错误", "请输入大于0的数字！")
                return
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字（如1、0.5）！")
            return

        # 初始化计时
        if not self.is_running and not self.is_paused:
            self.remaining_time = minutes * 60
            self.start_time = time.time()
        elif self.is_paused:
            # 暂停后继续：更新开始时间（补偿暂停的时长）
            self.start_time = time.time() - (minutes * 60 - self.remaining_time)
            self.is_paused = False

        self.is_running = True
        self.start_btn.config(state=tk.DISABLED)
        self.pause_btn.config(state=tk.NORMAL)
        self.update_countdown()

    def pause_timer(self):
        """暂停计时"""
        if self.is_running and not self.is_paused:
            self.is_paused = True
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(text="继续")
            # 清除定时器任务
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
        elif self.is_paused:
            # 从暂停状态继续
            self.start_timer()
            self.pause_btn.config(text="暂停")

    def reset_timer(self):
        """重置计时"""
        self.is_running = False
        self.is_paused = False
        self.remaining_time = 0
        self.countdown_label.config(text="00:00:00")
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED, text="暂停")
        # 清除定时器任务
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def update_countdown(self):
        """更新倒计时显示"""
        if self.is_running and not self.is_paused:
            # 计算剩余时间
            elapsed = time.time() - self.start_time
            self.remaining_time = max(0, (float(self.time_entry.get()) * 60) - elapsed)
            # 格式化并显示
            self.countdown_label.config(text=self.format_time(self.remaining_time))

            if self.remaining_time <= 0:
                # 计时结束：弹窗提醒 + 声音
                self.is_running = False
                self.start_btn.config(state=tk.NORMAL)
                self.pause_btn.config(state=tk.DISABLED)
                # Windows 提示音（短音）
                winsound.Beep(1000, 1000)  # 频率1000Hz，时长1000ms
                messagebox.showinfo("计时结束", "时间到！")
                return

            # 每100ms更新一次（避免高频刷新）
            self.timer_id = self.root.after(100, self.update_countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = PopupTimer(root)
    root.mainloop()