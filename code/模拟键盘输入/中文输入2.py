import pyautogui
import time



content = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            #长度不为0
            content.append(line)

print(f"列表长度：{len(content)}")
print(f"内容：{content}")

for con in content:
    pyautogui.typewrite(con)
    pyautogui.press('enter')


# import pyautogui
# import time
# from pywinauto import Desktop, Application  # 新增：Windows控件操作库
#
# # ========== 原有读取文件逻辑（保留） ==========
# content = []
# with open('input.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         if line:
#             # 长度不为0才加入列表
#             content.append(line)
#
# print(f"列表长度：{len(content)}")
# print(f"内容：{content}")
#
# # ========== 新增：Windows控件写入中文逻辑 ==========
# def write_chinese_windows(text, target_window_title=".*"):
#     """
#     向指定Windows窗口输入中文（不依赖粘贴/输入法）
#     :param text: 要输入的文本
#     :param target_window_title: 目标窗口标题（支持正则，如"记事本"填".*记事本.*"）
#     """
#     try:
#         # 连接已打开的目标窗口（按标题匹配）
#         app = Application(backend="uia").connect(title_re=target_window_title)
#         # 获取当前激活的输入控件（通用写法，适配多数输入框）
#         input_ctrl = app.window(title_re=target_window_title).focused_control()
#     except:
#         # 如果没找到指定窗口，默认向当前激活的窗口输入（依赖pyautogui激活）
#         input_ctrl = None
#
#     if input_ctrl:
#         # 方式1：直接通过控件写入（最优）
#         input_ctrl.type_keys(text, with_spaces=True, with_newlines=True)
#     else:
#         # 兼容方案：若无法定位控件，仍用pyautogui激活后写入
#         pyautogui.typewrite(text)  # pywinauto的typewrite兼容中文
#
# # ========== 核心：逐行输入中文 ==========
# # 1. 预留5秒时间：让你点击目标输入窗口（如记事本、网页输入框）
# print("请在5秒内点击要输入内容的窗口...")
# time.sleep(3)
#
# # 2. 逐行输入文件内容（替换原pyautogui.write(con)）
# for con in content:
#     # 关键修改：用Windows控件写入中文，替代原pyautogui.write(con)
#     write_chinese_windows(con)
#     pyautogui.press('enter')  # 保留原有按回车的逻辑
#     time.sleep(0.5)  # 新增：每行输入后间隔0.5秒，避免输入过快