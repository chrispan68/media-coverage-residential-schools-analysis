from TikTokApi import TikTokApi
import json
from tqdm import tqdm

api = TikTokApi(custom_verify_fp="verify_25fe94a19de666a71016322e2a5c9577", use_test_endpoints=True)
username = 'nichrichie'
user = api.user(username=username)

data = []
for video in tqdm(user.videos(count=1100)):
    try:
        data.append(video.as_dict)
    except:
        continue

with open('data/' + username + '_data.json', 'w') as f:
    json.dump(data, f, indent=4)