import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import matplotlib.pyplot as plt

# ToTensor() converts a PIL image or NumPy ndarray into a FloatTensor.
# and scales the image’s pixel intensity values in the range [0., 1.]
# Lambda() applies self-defined transform
# lambda defines an anonymous function, y is the parameter
# input.scatter__(dim, index, src) changes the value of input at index in dimension "dim" to the value "src"
# index must be a tensor, dim=0 corresponds to the first dimension
training_data = datasets.FashionMNIST(
    root="data",  # root is the path where the train/test data is stored
    train=True,  # train specifies training or test dataset
    download=True,  # download=True downloads the data from the internet if it’s not available at root
    transform=ToTensor(),  # It specify the feature and label transformations
    # target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),  # It specify the feature and label transformations
    # target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
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

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)  # shuffle=True将随机打乱数据再划分batch
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

# Display image and label
train_features, train_labels = next(iter(train_dataloader))  # iter()创建迭代器对象，next()返回迭代器下一个元素
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="jet")
plt.show()
print(f"Label: {label}")
