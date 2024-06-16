import os
import shutil
import random

def split_dataset(source_folder, train_folder, test_folder, split_ratio=0.8):
    # 创建目标目录（如果不存在）
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # 遍历源文件夹中的每个子文件夹
    for subdir in os.listdir(source_folder):
        subdir_path = os.path.join(source_folder, subdir)
        if os.path.isdir(subdir_path):
            images = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]

            # 打乱所有图片文件列表
            random.shuffle(images)

            # 按比例划分训练集和测试集
            split_index = int(len(images) * split_ratio)
            train_images = images[:split_index]
            test_images = images[split_index:]

            # 创建训练集和测试集子文件夹
            train_subdir = os.path.join(train_folder, subdir)
            test_subdir = os.path.join(test_folder, subdir)
            os.makedirs(train_subdir, exist_ok=True)
            os.makedirs(test_subdir, exist_ok=True)

            # 移动图片到训练集目录
            for image in train_images:
                shutil.copy(os.path.join(subdir_path, image), os.path.join(train_subdir, image))

            # 移动图片到测试集目录
            for image in test_images:
                shutil.copy(os.path.join(subdir_path, image), os.path.join(test_subdir, image))

            print(f"子文件夹 '{subdir}' 划分完毕：{len(train_images)} 张训练集图片，{len(test_images)} 张测试集图片")

source_dir = r"D:\desktop\imagecut\augimage - Copy"
train_dir = r"D:\desktop\imagecut\resnetdataset\train"
test_dir = r"D:\desktop\imagecut\resnetdataset\test"

split_dataset(source_dir, train_dir, test_dir)
