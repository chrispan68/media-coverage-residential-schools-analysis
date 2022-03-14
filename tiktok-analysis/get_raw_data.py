import json
import pandas as pd 
import itertools
import os 
import datetime
from tqdm import tqdm

data_full = pd.DataFrame(columns=['Username', 'Date Created', 'Num Likes', 'Num Shares', 'Num Comments', 'Num Views', 'Caption'])

for filename in tqdm(os.listdir('tiktok_analysis/data')):
    f = open(os.path.join('tiktok_analysis/data', filename))
    username = filename[:-10]
    data_user = json.load(f)
    for vid in data_user:
        vid_row = {}
        vid_row['Username'] = username
        vid_row['Date Created'] = datetime.datetime.fromtimestamp(vid['createTime'])
        vid_row['Num Likes'] = vid['stats']['diggCount']
        vid_row['Num Shares'] = vid['stats']['shareCount']
        vid_row['Num Comments'] = vid['stats']['commentCount']
        vid_row['Num Views'] = vid['stats']['playCount']
        vid_row['Caption'] = vid['desc']
        data_full = data_full.append(vid_row, ignore_index=True)
data_full.to_csv('tiktok_analysis/data/tiktok_data_raw.csv')


