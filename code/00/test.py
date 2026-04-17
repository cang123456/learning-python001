from pynput import keyboard

def on_press(key):
    """按键按下时触发"""
    try:
        print(f'按下普通键: {key.char}')
    except AttributeError:
        print(f'按下特殊键: {key}')

def on_release(key):
    """按键松开时触发"""
    print(f'松开键: {key}')
    if key == keyboard.Key.esc:
        # 按下 esc 退出监听
        return False

# 启动键盘监听
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

















