import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image


# Used to store the dataset in a directory img_dir
# Labels are stored in a CSV file annotations_file

class CustomImageDataset(Dataset):
    # The __init__ function is run once when instantiating the Dataset object.
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)  # Store the data in a DataFrame
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    # The __len__ function returns the number of samples in our dataset.
    def __len__(self):
        return len(self.img_labels)

    # The __getitem__ function loads and returns a sample from the dataset at the given index idx
    # Including image and the corresponding label
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])  # ???
        image = read_image(img_path)  # read image and transfer it to a tensor
        label = self.img_labels.iloc(idx, 1)  # retrieve the corresponding label
        if self.transform:
            image = self.transform(image)  # used to modify features
        if self.target_transform:
            image = self.target_transform(label)  # used to modify labels
        return image, label
