import tarfile

def extract_tar(tar_file, extract_to):
    with tarfile.open(tar_file, 'r') as tar:
        tar.extractall(path=extract_to)

# 使用示例
tar_file = r'D:\desktop\classification-pytorch-2.0\classification-pytorch-2.0\model_data\starnet_s4.pth.tar'
extract_to = r'D:\desktop\classification-pytorch-2.0\classification-pytorch-2.0\model_data'  # 解压到目标目录
extract_tar(tar_file, extract_to)
