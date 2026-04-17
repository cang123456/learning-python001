import pyautogui
import time
import sys


def move_mouse_periodically(interval=30, move_distance=50):
    """
    每隔指定时间左右移动鼠标
    :param interval: 移动间隔（秒），默认30秒
    :param move_distance: 每次移动的像素距离，默认50像素
    """
    print("鼠标自动移动程序已启动！")
    print(f"每隔{interval}秒左右移动鼠标{move_distance}像素")
    print("按下 Ctrl+C 可终止程序\n")

    try:
        # 初始化移动方向（True为右，False为左）
        move_right = True

        while True:
            # 根据方向移动鼠标（相对当前位置）
            if move_right:
                pyautogui.moveRel(move_distance, 0, duration=0.5)  # 右移，duration是移动耗时（秒）
                print(f"[{time.ctime()}] 鼠标右移{move_distance}像素")
            else:
                pyautogui.moveRel(-move_distance, 0, duration=0.5)  # 左移
                print(f"[{time.ctime()}] 鼠标左移{move_distance}像素")

            # 切换下一次移动方向
            move_right = not move_right

            # 等待指定间隔时间
            time.sleep(interval)

    except KeyboardInterrupt:
        # 捕获Ctrl+C终止信号
        print("\n程序已被用户终止，退出成功！")
        sys.exit(0)
    except Exception as e:
        # 捕获其他异常
        print(f"\n程序运行出错：{str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    # 调用函数，可修改interval调整间隔，move_distance调整移动距离
    move_mouse_periodically(interval=30, move_distance=1000)