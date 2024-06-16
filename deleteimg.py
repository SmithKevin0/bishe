import os

def delete_images_with_keywords(directory, keywords):
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否包含任何关键字
        if any(keyword in filename for keyword in keywords):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

# 目标目录
directory = r"D:\desktop\imagecut\cut - Copy\transparent20"
# 关键字列表
keywords = ["flip", "rot"]

delete_images_with_keywords(directory, keywords)
