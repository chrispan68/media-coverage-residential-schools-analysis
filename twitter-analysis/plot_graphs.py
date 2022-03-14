import pandas as pd
import os
from tqdm import tqdm
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt

full_df = []
for filename in os.listdir('twitter_analysis/data'):
    full_df.append(pd.read_csv('twitter_analysis/data/' + filename))
twitter_data = pd.concat(full_df)
times = [int(x / 1000) for x in twitter_data['created_at']]
times = [dt.datetime.utcfromtimestamp(d) for d in times]

names = ['Tweets', 'Likes', 'Replies', 'Retweets']
col_names = ['ntweets', 'nlikes', 'nreplies', 'nretweets']

for name, col_name in zip(names, col_names):
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    if col_name == 'ntweets':
        weights = None
    else: 
        weights = twitter_data[col_name]
    plt.hist(times, bins=50,weights=weights)
    plt.xlabel('Date')
    plt.ylabel('Number of ' + name)
    plt.title('Number of ' + name + ' Over Time')
    plt.savefig('twitter_analysis/results/'+ col_name + '.png')
    plt.clf()