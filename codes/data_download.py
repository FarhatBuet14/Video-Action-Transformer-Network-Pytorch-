import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import cv2
import pytube
import json

root_dir = "../"
data_dir = os.path.join(root_dir, "data", "AVA")

train_link = pd.read_csv(os.path.join(data_dir, "ava_ytids_train_v1.0.txt"))
test_link = pd.read_csv(os.path.join(data_dir, "ava_ytids_test_v1.0.txt"))

train_link = [link for link in train_link.iloc[:, 0]]
test_link = [link for link in test_link.iloc[:, 0]]

cant_dwn = []

for dom in ["train", "test"]:
    if(dom == "train"): file = train_link
    else: file = test_link
    video_dir = os.path.join(data_dir, dom)
    if(not os.path.exists(video_dir)): os.mkdir(video_dir)
    for i in tqdm(range(len(file))):
        try:
            youtube = pytube.YouTube("https://www.youtube.com/watch?v=" + file[i])
            video = youtube.streams.first()
            video.download(video_dir)
        except: 
            cant_dwn.append([dom, file[i]])

with open(data_dir + '/download_error_list.txt', 'w') as outfile:
    json.dump(cant_dwn, outfile)

print("Finished")