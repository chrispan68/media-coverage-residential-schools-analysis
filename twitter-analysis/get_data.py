import twint
import pandas as pd
for username in ['RussDiabo', 'charitieropati', 'TailyrIrvine', 'jessewente']:
    df = []
    since = '2021-05-01'
    until = '2021-08-01'
    e_cnt = 0
    while e_cnt < 5 or ((not '2021-05-0' in until) and (e_cnt < 20)): 
        config = twint.Config()
        config.Username = username
        config.Since = since
        config.Until = until
        config.Limit = 400
        config.Pandas = True
        twint.run.Search(config)
        try:
            tweets_df = twint.storage.panda.Tweets_df
            df.append(tweets_df)
            until_new = tweets_df['date'].iloc[-1]
            if until_new == until:
                break
            until = until_new
            e_cnt = 0
        except Exception as e:
            e_cnt += 1
    df = pd.concat(df)
    df.to_csv('twitter_analysis/data/' + username + '.csv')