import os
from PIL import Image

# 指定目录路径
input_dir = r"D:\desktop\imagecut\cut - Copy\transparent20"

# 创建增强后的图像文件夹
output_dir = os.path.join(input_dir, "augmented")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取目录下所有图片文件
image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)) and f.endswith(('jpg', 'jpeg', 'png'))]

# 定义增强方法
def augment_image(image_path, output_path, count):
    image = Image.open(image_path)
    augmentations = [
        ("_flip_h", image.transpose(Image.FLIP_LEFT_RIGHT)),
        ("_flip_v", image.transpose(Image.FLIP_TOP_BOTTOM)),
        ("_rot_90", image.rotate(90, expand=True)),
        ("_rot_180", image.rotate(180, expand=True)),
        ("_rot_270", image.rotate(270, expand=True)),
    ]

    for suffix, aug_image in augmentations:
        aug_image.save(os.path.join(output_path, f"{os.path.splitext(os.path.basename(image_path))[0]}{suffix}_{count}.png"))

# 获取已有图片数量
existing_image_count = len(image_files)
if existing_image_count >= 1000:
    print(f"已有图片数量为{existing_image_count}，不需要进行数据增强。")
else:
    count = 0
    while len(os.listdir(output_dir)) + existing_image_count < 1000:
        for image_file in image_files:
            augment_image(os.path.join(input_dir, image_file), output_dir, count)
            count += 1
            if len(os.listdir(output_dir)) + existing_image_count >= 1000:
                break

print(f"数据增强完成，总图片数量: {len(os.listdir(output_dir)) + existing_image_count}")
