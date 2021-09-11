import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


# To use the model, we pass it the input data. This executes the model’s forward,
# along with some background operations. Do not call model.forward() directly!
class NeuralNetwork(nn.Module):  # 子类NeuralNetwork继承自父类nn.Module
    def __init__(self):
        super(NeuralNetwork, self).__init__()  # 先找到父类，然后把子类对象转为父类对象，再调用父类的方法
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),  # 全连接层，以矩阵线性运算实现
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


device = 'cuda' if torch.cuda.is_available() else 'cpu'
# str.format()用{}与:代替%来站位，并在占位处显示format()设定的参数
# 具体用法参见 https://www.runoob.com/python/att-string-format.html
print(f"Using {device} device")

model = NeuralNetwork().to(device)  # 创建NeuralNetwork子类，并使用继承的方法
print("Model structure: ", model, "\n\n")
for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values: {param[:2]}\n")

X = torch.rand(3, 28, 28, device=device)  # a sample mini-batch of 3 images of size 28x28
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)  # 创建Softmax对象，再用于处理数据
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")
