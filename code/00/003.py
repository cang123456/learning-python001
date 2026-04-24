import os
import shutil
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading


# 备份新文件到目标文件夹，并记录日志
def backup_new_files(source_folder, backup_folder, log_file, info_text):
    backup_count = 0  # 记录备份文件数量
    try:
        with open(log_file, "a") as log:
            log.write(f"备份开始时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} (北京时间)\n")
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    source_file = os.path.join(root, file)
                    backup_file = os.path.join(backup_folder, os.path.relpath(source_file, source_folder))
                    if not os.path.exists(backup_file):
                        backup_dir = os.path.dirname(backup_file)
                        if not os.path.exists(backup_dir):
                            os.makedirs(backup_dir)
                        shutil.copy2(source_file, backup_file)
                        log.write(f"备份文件: {source_file} -> {backup_file}\n")
                        info_text.insert(tk.END,
                                         f"已备份文件: {source_file} -> {backup_file} [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]\n")
                        backup_count += 1
            log.write("备份完成\n")
            if backup_count > 0:
                info_text.insert(tk.END, f"备份完成 [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]\n")
    except Exception as e:
        messagebox.showerror("错误", f"备份过程中发生错误：{str(e)}")


# 监听文件夹变化，并备份新增文件
def watch_folder(source_folder, backup_folder, interval, log_folder, info_text, status_label):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    today = time.strftime("%Y%m%d", time.localtime())
    log_file = os.path.join(log_folder, f"{today}.log")
    info_text.insert(tk.END, f"日志文件路径: {log_file}\n")

    status_label.config(text="备份程序已运行")
    while True:
        backup_new_files(source_folder, backup_folder, log_file, info_text)
        time.sleep(interval)


# 开始备份按钮点击事件
def start_backup(source_folder_entry, backup_folder_entry, interval_entry, info_text, start_button, status_label,
                 browse_source_button, browse_backup_button):
    source_folder = source_folder_entry.get().strip()
    backup_folder = backup_folder_entry.get().strip()
    interval = interval_entry.get().strip()

    if not source_folder:
        messagebox.showerror("错误", "请选择源文件夹路径")
        return
    if not os.path.exists(source_folder):
        messagebox.showerror("错误", "源文件夹不存在")
        return
    if not backup_folder:
        messagebox.showerror("错误", "请选择备份文件夹路径")
        return
    if not os.path.exists(backup_folder):
        messagebox.showerror("错误", "备份文件夹不存在")
        return
    try:
        if not interval:
            interval = 360
            messagebox.showwarning("警告",
                                   f"检测到你未输入备份间隔时间，默认{interval}秒 [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]")
        else:
            interval = int(interval)
            if interval <= 0:
                raise ValueError
    except ValueError:
        messagebox.showerror("错误", "备份间隔必须是一个大于零的整数")
        return

    start_button.config(state=tk.DISABLED)  # 禁用开始备份按钮
    browse_source_button.config(state=tk.DISABLED)  # 禁用选择源文件夹按钮
    browse_backup_button.config(state=tk.DISABLED)  # 禁用选择备份文件夹按钮
    interval_entry.config(state=tk.DISABLED)  # 禁用备份间隔输入框

    # 启动备份线程
    backup_thread = threading.Thread(target=watch_folder,
                                     args=(source_folder, backup_folder, interval, "logs", info_text, status_label))
    backup_thread.daemon = True
    backup_thread.start()


# 选择源文件夹按钮点击事件
def select_source_folder(source_folder_entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        source_folder_entry.delete(0, tk.END)
        source_folder_entry.insert(0, folder_path)


# 选择备份文件夹按钮点击事件
def select_backup_folder(backup_folder_entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        backup_folder_entry.delete(0, tk.END)
        backup_folder_entry.insert(0, folder_path)


# 创建 GUI 窗口
def create_gui():
    root = tk.Tk()
    root.title("文件备份小工具 v1.0 \nEmail:size18@foxmail.com")
    root.geometry("500x300")
    root.resizable(False, False)  # 禁止调整窗口大小

    tk.Label(root, text="源文件夹:", font=("Arial", 12)).place(x=20, y=20)
    source_folder_entry = tk.Entry(root, width=40, font=("Arial", 10))
    source_folder_entry.place(x=120, y=20)
    browse_source_button = tk.Button(root, text="选择文件夹", font=("Arial", 10),
                                     command=lambda: select_source_folder(source_folder_entry))
    browse_source_button.place(x=400, y=16)

    tk.Label(root, text="备份文件夹:", font=("Arial", 12)).place(x=20, y=60)
    backup_folder_entry = tk.Entry(root, width=40, font=("Arial", 10))
    backup_folder_entry.place(x=120, y=60)
    browse_backup_button = tk.Button(root, text="选择文件夹", font=("Arial", 10),
                                     command=lambda: select_backup_folder(backup_folder_entry))
    browse_backup_button.place(x=400, y=56)

    tk.Label(root, text="备份间隔（秒）:", font=("Arial", 12)).place(x=20, y=100)
    interval_entry = tk.Entry(root, font=("Arial", 10), width=10)
    interval_entry.place(x=180, y=100)
    interval_entry.insert(0, "360")  # 默认备份间隔时间为360秒

    info_text = tk.Text(root, height=8, width=60, font=("Arial", 10))
    info_text.place(x=20, y=140)

    status_label = tk.Label(root, text="", font=("Arial", 12))
    status_label.place(x=20, y=260)

    start_button = tk.Button(root, text="开始备份", font=("Arial", 12),
                             command=lambda: start_backup(source_folder_entry, backup_folder_entry, interval_entry,
                                                          info_text, start_button, status_label, browse_source_button,
                                                          browse_backup_button))
    start_button.place(x=200, y=260)

    root.mainloop()


if __name__ == "__main__":
    create_gui()