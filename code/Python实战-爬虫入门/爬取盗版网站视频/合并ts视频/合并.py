import os
import subprocess
import glob
import time

# ===================== 配置项（根据你的实际路径修改）=====================
# 1. 已下载的.ts文件所在目录（不要有中文/空格）
TS_DIR = r"test"
# 2. 合并后的输出视频文件名
OUTPUT_VIDEO = r"test/merged_video.mp4"
# 3. FFmpeg路径（若已配置环境变量，直接填"ffmpeg"即可；否则填完整路径）
FFMPEG_PATH = "ffmpeg"  # 环境变量已配置 → 直接用；否则改为 r"D:\ffmpeg\bin\ffmpeg.exe"

# 用cmd合并的命令
# ffmpeg -f concat -safe 0 -i ts_list.txt -c copy output.mp4

# ===================== 核心函数 =====================
def create_ts_list(ts_dir, list_file="ts_list.txt"):
    """
    自动创建.ts文件列表（按数字顺序排序，避免合并后顺序错乱）
    :param ts_dir: .ts文件所在目录
    :param list_file: 生成的列表文件名
    :return: 列表文件的完整路径
    """
    # 1. 获取所有.ts文件，按数字序号排序（关键：ts_001.ts → ts_002.ts...）
    ts_files = glob.glob(os.path.join(ts_dir, "ts_*.ts"))
    # 按文件名中的数字排序（处理ts_001.ts、ts_010.ts等格式）
    ts_files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x)))))

    # 2. 生成列表文件
    list_file_path = list_file
    with open(list_file_path, "w",encoding='utf-8') as f:
        for ts_file in ts_files:
            # 写入FFmpeg要求的格式：file '绝对路径'
            f.write(f"file '{ts_file}'\n")

    print(f"✅ 已生成.ts列表文件：{list_file_path}")
    print(f"📄 共找到 {len(ts_files)} 个.ts切片")
    return list_file_path


def merge_ts_with_ffmpeg(ts_dir, output_video, ffmpeg_path):
    """
    调用FFmpeg合并.ts文件
    :param ts_dir: .ts文件所在目录
    :param output_video: 输出视频路径
    :param ffmpeg_path: FFmpeg可执行文件路径
    """
    # 1. 先创建.ts列表文件
    list_file = create_ts_list(ts_dir)

    # 2. 构造FFmpeg合并命令
    # 核心命令：ffmpeg -f concat -safe 0 -i ts_list.txt -c copy -bsf:a aac_adtstoasc output.mp4
    cmd = [
        ffmpeg_path,
        "-f", "concat",  # 指定拼接模式
        "-safe", "0",  # 允许访问本地文件
        "-i", list_file,  # 输入的.ts列表文件
        "-c", "copy",  # 无损复制音视频流（不重新编码）
        "-bsf:a", "aac_adtstoasc",  # 修复音频格式兼容问题
        "-y",  # 覆盖已存在的输出文件（无需确认）
        output_video  # 输出视频路径
    ]

    try:
        # 执行FFmpeg命令，捕获输出信息
        print("\n🚀 开始合并视频...")
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            shell=True  # Windows系统建议加shell=True
        )

        # 检查执行结果
        if result.returncode == 0:
            print(f"\n✅ 视频合并成功！输出文件：{output_video}")
            # 可选：删除临时的列表文件
            os.remove(list_file)
            print("🗑️ 已清理临时列表文件")
        else:
            print(f"\n❌ 合并失败！FFmpeg报错：{result.stderr}")
    except Exception as e:
        print(f"\n❌ 程序执行异常：{str(e)}")


# ===================== 执行合并 =====================
if __name__ == "__main__":
    # 检查.ts目录是否存在
    if not os.path.exists(TS_DIR):
        print(f"❌ 错误：.ts文件目录 {TS_DIR} 不存在！")
    else:
        merge_ts_with_ffmpeg(TS_DIR, OUTPUT_VIDEO, FFMPEG_PATH)

    print("="*20,"运行成功","="*20)
    print("3秒后关闭")
    time.sleep(3)