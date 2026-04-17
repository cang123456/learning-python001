import os
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor
from moviepy.editor import VideoFileClip, AudioFileClip


def merge_audio_video(video_path, audio_path, output_path):
    """
    将音频文件和视频文件合并

    Args:
        video_path (str): 视频文件路径
        audio_path (str): 音频文件路径
        output_path (str): 输出文件路径
    """
    # 加载视频和音频文件
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # 如果音频比视频长，裁剪音频
    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration)

    # 设置视频的音频
    final_clip = video_clip.set_audio(audio_clip)

    # 写入输出文件，使用多线程加快处理速度
    final_clip.write_videofile(
        output_path, 
        codec='libx264', 
        audio_codec='aac',
        threads=4,  # 使用多线程
        preset='ultrafast'  # 使用最快的编码预设
    )

    # 关闭资源
    video_clip.close()
    audio_clip.close()
    final_clip.close()


def batch_merge(directory, video_ext='.mp4', audio_ext='.mp3', output_dir=None):
    """
    批量合并目录下的音频和视频文件

    Args:
        directory (str): 包含音视频文件的目录
        video_ext (str): 视频文件扩展名
        audio_ext (str): 音频文件扩展名
        output_dir (str): 输出目录，默认为原目录
    """
    if output_dir is None:
        output_dir = directory

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 获取所有视频文件
    video_files = [f for f in os.listdir(directory) if f.endswith(video_ext)]

    merged_count = 0
    failed_count = 0
    
    # 使用线程池并发处理多个文件
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for video_file in video_files:
            # 构建对应的音频文件名（假设名称相同，扩展名不同）
            base_name = os.path.splitext(video_file)[0]
            audio_file = base_name + audio_ext

            video_path = os.path.join(directory, video_file)
            audio_path = os.path.join(directory, audio_file)
            output_path = os.path.join(output_dir, base_name + "_merged" + video_ext)

            # 检查音频文件是否存在
            if os.path.exists(audio_path):
                print(f"正在合并: {video_file} + {audio_file}")
                # 提交任务到线程池
                future = executor.submit(merge_audio_video, video_path, audio_path, output_path)
                futures.append((future, output_path, video_file, audio_file))
            else:
                print(f"未找到对应的音频文件: {audio_file}")
                failed_count += 1
        
        # 等待所有任务完成
        for future, output_path, video_file, audio_file in futures:
            try:
                future.result()  # 获取结果以触发异常
                print(f"合并成功: {output_path}")
                merged_count += 1
            except Exception as e:
                print(f"合并失败 {video_file} + {audio_file}: {str(e)}")
                failed_count += 1

    print(f"总共合并了 {merged_count} 对音视频文件，失败 {failed_count} 对")


def main():
    parser = argparse.ArgumentParser(description='合并音频和视频文件')
    parser.add_argument('-d', '--directory', default='.',
                        help='包含音视频文件的目录 (默认: 当前目录)')
    parser.add_argument('-v', '--video_ext', default='.mp4',
                        help='视频文件扩展名 (默认: .mp4)')
    parser.add_argument('-a', '--audio_ext', default='.mp3',
                        help='音频文件扩展名 (默认: .mp3)')
    parser.add_argument('-o', '--output_dir',
                        help='输出目录 (默认: 原目录)')

    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print(f"错误: 目录 '{args.directory}' 不存在")
        return

    batch_merge(args.directory, args.video_ext, args.audio_ext,args.output_dir)


if __name__ == "__main__":
    # 示例用法
    print("音视频合并工具")
    print("=" * 30)

    # 如果直接运行此脚本，使用当前目录
    # 您也可以通过命令行参数指定目录和其他选项
    main()