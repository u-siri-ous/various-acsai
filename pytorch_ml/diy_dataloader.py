'''
Create a dataloader class

Label example:      (image, class)
img1.jpg, 0
img2.jpg, 1
img3.jpg, 2
img4.jpg, 0
'''

import os
import pandas as pd
from torchvision.io import read_image
from torch.utils.data import Dataset

class MyDatasetLoader(Dataset):
    def __init__(self, labels, img_dir, transform=None):
        self.img_dir = img_dir
        self.transform = transform
        self.labels = pd.read_csv(labels)   # labels are text
        # REM: image segmentation -> label transform (unneeded here)

    def __len__(self):              # len(dataset)
        return len(self.labels)     # as we already know a table-like repr of dataset (pandas)

    def __getitem__(self, index):   # how to handle data in dataset
    # read our images from the disk
        # create the images path
        # e.g. img_dir = 'data/'
        #      for file name, iloc allows us to select an element from a pandas dataframe in [row, column]
        # out = 'data/img1.jpg' 
        imgs_path = os.join(self.img_dir, self.labels.iloc[index, 0])   

        # read image through path
        image = read_image(imgs_path)   # several ways to do this, basically cv2.imread(imgs_path)

        # read the labels
        label = self.labels.iloc[index, 1]

        # apply transformation(s)
        if self.transform:
            image = self.transform(image)

        return image, label