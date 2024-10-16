import torch
print(torch.__version__)         # 显示当前安装的 PyTorch 版本
print(torch.version.cuda)        # 显示与 PyTorch 兼容的 CUDA 版本
print(torch.cuda.is_available())  # 检查 CUDA 是否可用
