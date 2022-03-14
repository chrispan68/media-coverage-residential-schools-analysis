import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d1 = json.load(open('news_analysis/news-articles-residential-school-page0.json', 'r'))
d2 = json.load(open('news_analysis/news-articles-residential-school-page1.json', 'r'))

total_data = d1['articles'] + d2['articles']

text = ""
for data in total_data:
    for keyword in data['keywords']:
        text += keyword['name'] + " "

word_cloud = WordCloud(collocations=False, background_color='black', width=2000, height=1000).generate(text)
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(word_cloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()