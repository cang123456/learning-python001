import pyautogui
import time


def pyautogui_basic():
    """pyautogui基本操作"""
    # 安全特性：鼠标移动到屏幕左上角会触发失败安全模式
    pyautogui.FAILSAFE = True

    # 1. 输入文本
    time.sleep(2)
    pyautogui.write("Hello from pyautogui!", interval=0.1)  # 每个字符间隔0.1秒

    # 2. 按键操作
    pyautogui.press('enter')  # 按回车
    pyautogui.press(['tab', 'tab', 'enter'])  # 按多个键

    # 3. 组合键
    pyautogui.hotkey('ctrl', 'c')  # 复制
    pyautogui.hotkey('ctrl', 'v')  # 粘贴
    pyautogui.hotkey('alt', 'tab')  # 切换窗口


def pyautogui_advanced():
    """pyautogui高级操作"""
    # 4. 特殊键
    pyautogui.press('f5')  # 刷新
    pyautogui.press('volumeup')  # 音量+
    pyautogui.press('volumedown')  # 音量-

    # 5. 按键并按住
    pyautogui.keyDown('shift')  # 按住shift
    pyautogui.write('uppercase')
    pyautogui.keyUp('shift')  # 松开shift

    # 6. 模拟快捷键输入密码
    def input_password():
        pyautogui.write("mysecretpassword", interval=0.05)
        pyautogui.press('enter')

    # 7. 带间隔的多次输入
    for i in range(3):
        pyautogui.write(f"Message {i + 1}")
        pyautogui.press('enter')
        time.sleep(1)


def pyautogui_special_chars():
    """输入特殊字符"""
    # 输入标点符号
    special_text = "Hello! @#$%^&*()_+{}|:\"<>?~`[]\\;',./"
    pyautogui.write(special_text, interval=0.05)

    # 中文输入（需要系统中安装中文输入法）
    # pyautogui.write("你好世界")  # 直接输入中文


def auto_form_fill():
    """自动填写表单"""
    time.sleep(3)

    # 填写表单字段
    fields = [
        ("John Doe", 0.2),
        ("john@example.com", 0.2),
        ("1234567890", 0.1),
        ("This is a test message.", 0.05)
    ]

    for text, interval in fields:
        pyautogui.write(text, interval=interval)
        pyautogui.press('tab')
        time.sleep(0.5)

    # 提交表单
    pyautogui.press('enter')


if __name__ == "__main__":
    pyautogui_basic()
    # pyautogui_advanced()
    # auto_form_fill()AIAI