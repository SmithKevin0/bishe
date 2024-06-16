import os


def delete_images(directory, keep_range):
    # 列出目录中的所有文件
    files = os.listdir(directory)

    # 确定需要保留的文件名关键字
    keep_files = [str(i) for i in range(keep_range[0], keep_range[1] + 1)]

    # 初始化删除计数
    delete_count = 0

    # 遍历文件并删除不在保留范围内的文件
    for file in files:
        if file.endswith(".jpg") and not any(keyword in file for keyword in keep_files):
            file_path = os.path.join(directory, file)
            os.remove(file_path)
            delete_count += 1
            print(f"Deleted: {file}")

        # 如果删除的文件达到要求数量（删除至目录剩下1500张），则停止
        if delete_count >= (len(files) - 1500):
            break

    print(f"Total deleted files: {delete_count}")


# 设置目录路径和保留范围
directory = r"D:\desktop\imagecut\augimage\white25"
keep_range = (1101, 1153)

# 调用函数执行删除操作
delete_images(directory, keep_range)
