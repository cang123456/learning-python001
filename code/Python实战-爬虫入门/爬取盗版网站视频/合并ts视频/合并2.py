import os
import subprocess
import glob


ts_dir="test"                                              # TS文件所在目录
output_file="output"                                         # 输出文件路径



ts_file = os.path.join(output_file, "ts_list.txt")
os.open(ts_file, os.O_CREAT)

with open(ts_file, "w", encoding="utf-8") as f:
    for ts_file in ts_dir:
        # abs_ts_path = os.path.join(ts_dir, ts_file)
        # f.write(f"file '{abs_ts_path}'\n")
        print(len(ts_dir))

# 4. 构造FFmpeg合并命令（-c copy 直接拷贝流，无重新编码，速度快）

# 5. 执行FFmpeg命令


# 6. 检查执行结果




    #
    # filelist_path = os.path.join(ts_dir, "filelist.txt")
    # try:
    #
    #     print(f"✅ 已生成文件列表：{filelist_path}")
    #
    #
    #     ffmpeg_cmd = [
    #         ffmpeg_path,
    #         "-f", "concat",  # 指定concat协议
    #         "-safe", "0",  # 允许访问绝对路径文件
    #         "-i", filelist_path,  # 输入文件列表
    #         "-c", "copy",  # 直接拷贝音频/视频流（无画质损失）
    #         "-y",  # 覆盖已存在的输出文件
    #         output_file  # 输出文件
    #     ]
    #
    #
    #     print(f"🚀 开始合并TS文件，输出路径：{output_file}")
    #     result = subprocess.run(
    #         ffmpeg_cmd,
    #         stdout=subprocess.PIPE,  # 捕获标准输出
    #         stderr=subprocess.PIPE,  # 捕获错误输出
    #         encoding="utf-8"  # 编码格式
    #     )
    #
    #
    #     if result.returncode == 0:
    #         print("✅ TS文件合并完成！")
    #         # 可选：删除临时的filelist.txt
    #         os.remove(filelist_path)
    #         print(f"🗑️ 已清理临时文件：{filelist_path}")
    #         return True
    #     else:
    #         print(f"❌ FFmpeg执行失败：{result.stderr}")
    #         return False
    #
    # except Exception as e:
    #     print(f"❌ 合并过程出错：{str(e)}")
    #     return False
    #

