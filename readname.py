import os

# 指定目录路径
directory = r"D:\desktop\imagecut\resnetdataset\train"

try:
    # 获取子文件夹名称列表
    subfolder_names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    # 竖排显示子文件夹名称
    for name in subfolder_names:
        print(name)
except FileNotFoundError:
    print("指定的目录路径不存在。请检查路径是否正确。")
except Exception as e:
    print(f"发生错误: {e}")
