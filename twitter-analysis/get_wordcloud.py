from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import os

full_df = []
for filename in os.listdir('twitter_analysis/data'):
    full_df.append(pd.read_csv('twitter_analysis/data/' + filename))
twitter_data = pd.concat(full_df)

text = ""
for tweet in twitter_data['tweet']:
    if 'residential' in tweet.lower() and 'school' in tweet.lower():
        text += ' ' + tweet + ' '


word_cloud = WordCloud(collocations=False, background_color='black', width=2000, height=1000).generate(text)
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(word_cloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()