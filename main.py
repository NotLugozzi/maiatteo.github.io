import requests
import json
from jinja2 import Template
map_id = "280304"
response = requests.get(f'https://api.codetabs.com/v1/proxy?quest=https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=it&page=1')
pizzi = requests.get(f"https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=us&search=sionpizzi")
if response.status_code == 200:
    scores_dict = response.json()
    pizzi_dict = pizzi.json()
    #print(pizzi_dict)
    #print(scores_dict) # godo
    scores = scores_dict['scores'][:10]
    pizziscore = pizzi_dict["scores"][:1]
    scores.extend(pizziscore)
    print(scores)
    with open('scores.json', 'w', encoding="utf-16") as f:
     json.dump(scores, f)
    print("json salvato")
    scores.sort(key=lambda score: score['baseScore'], reverse=True)
    #placeholder
    template = Template("""
    <html>
    <head>
        <title>BSEUC Qualifiers Italia</title>
        <style>
           table, th, td {
           border: 2px solid black;
           text-align: center;
           }
           h1, h2, h3{
           text-align: center;
           }
           .center {
            margin-left: auto;
            margin-right: auto;
            }
        </style>
    </head>
    <body>
        <h3>placeholder map name</h3>
        <table class="center">
        <tr>
            <th style="padding:10px">Player</th>
            <th style="padding:10px">Score</th>
            <th style="padding:10px">FC</th>
            <th style="padding:10px">Last Played Date</th>
        </tr>
        {% for score in scores %}
           <tr>
            <td>{{ score.leaderboardPlayerInfo.name }}</td>
            <td>{{ score.baseScore }}</td>
            <td>{{ score.fullCombo }}</td>
            <td>{{ score.timeSet }}</td>
          </tr>
          {% endfor %}
        </table>
      </body>
    </html>
    """)
    html = template.render(scores=scores)
    with open("index.html", "w", encoding="utf-16") as f:
     f.write(html)
else:
    print("An error occurred:", response.status_code)