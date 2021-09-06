import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(
    root="data",  # root is the path where the train/test data is stored
    train=True,  # train specifies training or test dataset
    download=True,  # download=True downloads the data from the internet if it’s not available at root
    transform=ToTensor()  # It specify the feature and label transformations
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8))  # figsize指定figure的宽和高，单位为英寸
cols, rows = 3, 3
for i in range(1, rows * cols + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()  # 随机选择一个图片的序号，item()将张量转为Python数值
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)  # 添加子图，并选择第i个进行操作
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")  # squeeze()去除tensor中为1的维度，把img变成二维；cmap控制颜色图谱
plt.show()
