import json
import pandas as pd

d1 = json.load(open('news_analysis/news-articles-residential-school-page0.json', 'r'))
d2 = json.load(open('news_analysis/news-articles-residential-school-page1.json', 'r'))

total_data = d1['articles'] + d2['articles']

csv_full = pd.DataFrame(columns=['Source', 'URL', 'Primary Author', 'Title', 'Positive Percentage', 'Neutral Percentage', 'Negative Percentage', 'Summary', 'Date'])
for article in total_data:
    row = {}
    row['Source'] = article['source']['domain']
    row['URL'] = article['url']
    row['Title'] = article['title']
    row['Positive Percentage'] = article['sentiment']['positive']
    row['Neutral Percentage'] = article['sentiment']['neutral']
    row['Negative Percentage'] = article['sentiment']['negative']
    row['Summmary'] = article['summary'].replace('\n', ' ')
    row['Date'] = article['pubDate']
    row['Primary Author'] = article['matchedAuthors'][0]['name'] if len(article['matchedAuthors']) > 0 else 'N/A'
    csv_full = csv_full.append(row, ignore_index=True)

csv_full.to_csv('news_analysis/news_data_raw.csv')