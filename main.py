import requests
import json
from jinja2 import Template
map_id = "408454"
response = requests.get(f'https://api.codetabs.com/v1/proxy?quest=https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=it&page=1')
if response.status_code == 200:
    scores_dict = response.json()
    # print(scores_dict) godo
    scores = scores_dict['scores'][:10]
    with open('scores.json', 'w', encoding="utf-16") as f:
     json.dump(scores, f)
    player_score = {
    'playerId': '12345',
    'country': 'other_country',
    'baseScore': 100000,
    'rank': 30,
    'pp': 1000,
    'leaderboardPlayerInfo': {
            'name': 'PlaceholderPizzi',
    }
    }
    scores.append(player_score)
    scores.sort(key=lambda score: score['rank'], reverse=False)
    #placeholder
    template = Template("""
    <html>
    <head>
        <title>zio pera</title>
    </head>
    <body>
        <h1>punteggio del godo</h1>
        <table>
        <tr>
            <th>Player</th>
            <th>Score</th>
        </tr>
        {% for score in scores %}
           <tr>
            <td>{{ score.leaderboardPlayerInfo.name }}</td>
            <td>{{ score.baseScore }}</td>
          </tr>
          {% endfor %}
        </table>
      </body>
    </html>
    """)
    html = template.render(scores=scores)
    with open("index.html", "w", encoding="utf-16") as f:
     f.write(html)
    with open('scores.json', 'w') as f:
     json.dump(scores, f)    
else:
    print("An error occurred:", response.status_code)