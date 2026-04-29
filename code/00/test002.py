import os

# 你要处理的文件夹
target_dir = r"D:\project\2026\forme001\forme001\wms-web\public\music"

# 100KB = 100 * 1024 字节
MAX_SIZE = 100 * 1024

# --------------------------
# 第一步：删除小于 100KB 的文件
# --------------------------
if not os.path.exists(target_dir):
    print(f"❌ 文件夹不存在：{target_dir}")
else:
    print(f"✅ 开始扫描并删除小于 100KB 的文件...\n")

    deleted_count = 0

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)

            # 删除小于 100KB 的文件
            if file_size < MAX_SIZE:
                try:
                    os.remove(file_path)
                    print(f"🗑️ 已删除（小于100KB）：{filename}")
                    deleted_count += 1
                except Exception as e:
                    print(f"❌ 删除失败：{filename}，{e}")

    print(f"\n🎉 清理完成！共删除文件：{deleted_count} 个")

# --------------------------
# 第二步：重命名为 mus1.mp3, mus2.mp3...
# --------------------------
print("\n---------------------------------")
print("✅ 开始重命名文件为 mus1.mp3 格式...\n")

# 重新获取剩下的文件
files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
files.sort()  # 按顺序重命名

rename_count = 0

for index, filename in enumerate(files, start=1):
    old_path = os.path.join(target_dir, filename)
    new_name = f"music{index}.mp3"
    new_path = os.path.join(target_dir, new_name)


    # 不重复命名
    if filename == new_name:
        continue

    try:
        os.rename(old_path, new_path)
        print(f"✅ 重命名：{filename} → {new_name}")
        rename_count += 1
    except Exception as e:
        print(f"❌ 重命名失败：{filename}，{e}")

print(f"\n🎉 全部完成！共重命名：{rename_count} 个文件")