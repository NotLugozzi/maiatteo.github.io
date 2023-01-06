import requests
import json
map_id = "323963"
response = requests.get(f'https://api.codetabs.com/v1/proxy?quest=https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=it&page=1')
if response.status_code == 200:
    scores_dict = response.json()
    # print(scores_dict) godo
    scores = scores_dict['scores'][:10]
    with open('scores.json', 'w') as f:
     json.dump(scores, f)
    player_score = {
    'playerId': '12345',
    'playerName': 'John Doe',
    'country': 'other_country',
    'rank': 100000,
    'pp': 1000,
    }
    scores.append(player_score)
    scores.sort(key=lambda score: score['rank'], reverse=True)
    with open('scores.json', 'w') as f:
     json.dump(scores, f)    
else:
    print("An error occurred:", response.status_code)
