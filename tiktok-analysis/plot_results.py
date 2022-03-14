import json
import matplotlib.pyplot as plt 
import numpy as np
from tqdm import tqdm
from datetime import datetime
import os

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
totals = []
for fname in ['nichrichie_data.json']: #tqdm(os.listdir('data')):
    filename = 'data/' + fname
    username = fname[:-10]

    with open(filename, 'r') as f:
        data = json.load(f)
    
    cur_totals = np.zeros(12)
    count = 0
    for vid in data:
        dt = datetime.fromtimestamp(vid['createTime'])
        if dt.year == 2021:
            cur_totals[dt.month - 1] += 1 #vid['stats']['playCount']
            count += 1 #vid['stats']['playCount']
    cur_totals /= count
    totals.append(cur_totals)

    totals = np.mean(np.array(totals), axis=0)
    plt.bar(month_names, totals)
    plt.xlabel('Month in 2021')
    plt.ylabel('Number of Videos (Relative)')
    plt.title('Relative Number of Videos per Month for ' + username)
    plt.savefig('results/' + username + '/rel_num_videos.png')
    plt.clf()