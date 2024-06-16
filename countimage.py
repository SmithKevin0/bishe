import os

def count_images_in_subfolders(path):
    # 获取指定路径下的所有子文件夹
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

    # 用于存储每个子文件夹中图片数量的字典
    image_counts = {}

    # 支持的图片扩展名
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')

    # 遍历每个子文件夹
    for folder in subfolders:
        # 获取子文件夹名称
        folder_name = os.path.basename(folder)
        # 获取子文件夹中的所有文件
        files = os.listdir(folder)
        # 统计图片数量
        image_count = sum(1 for file in files if file.lower().endswith(image_extensions))
        # 将统计结果保存到字典中
        image_counts[folder_name] = image_count

    return image_counts

if __name__ == "__main__":
    path = r"D:\desktop\Siamese-pytorch-master\Siamese-pytorch-master\datasets"
    image_counts = count_images_in_subfolders(path)
    for folder, count in image_counts.items():
        print(f"{folder} - {count} images")
