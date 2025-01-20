!pip install torchvision


from google.colab import drive
drive.mount("/content/drive")

from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision.transforms as T

image_path = "/content/drive/MyDrive/code_prac/detection_dataset.jpg"
image = Image.open(image_path)
plt.imshow(image)

def plot(imgs, with_orig=True, row_title=None, **imshow_kwargs):
    if not isinstance(imgs[0], list):
        imgs = [imgs]
        print(imgs)
        
        num_rows = len(imgs)
        print(num_rows)
        num_cols = len(imgs[0] + with_orig)
        fig, axs = plt.subplots(nrows=num_rows, ncols=num_cols, squeeze=False, figsize=(20, 8))
        for row_idx, row in enumerate(imgs):
            row = [imgs] + row if with_orig else row
            print(row)
            for col_idx, img in enumerate(row):
                ax = axs[row_idx, col_idx]
                print(ax)
                ax.imshow(np.asarray(img))

