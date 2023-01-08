import requests
import json
from jinja2 import Template
map_id = "379722"
response = requests.get(f'https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=it&page=1')
pizzi = requests.get(f"https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=us&search=sionpizzi")
def has_error_message(json_data):
    if isinstance(json_data, dict):
        return "errorMessage" in json_data and json_data["errorMessage"] == "No scores found"
    return False
if response.status_code == 200:
    scores_dict = response.json()
    pizzi_dict = pizzi.json()
    scores = scores_dict['scores'][:10]
    if has_error_message(pizzi_dict) == True:
      print("pizzi non trovato:nerd:")
    else:
      pizziscore = pizzi_dict["scores"][:1]
      scores.extend(pizziscore)
      print("pizzi trovato:tf:")

    #print(scores_dict) # godo
    #print(scores)
    print("scrivo scores.json")
    with open('scores.json', 'w', encoding="utf-16") as f:
     json.dump(scores, f)
    print("scores.json scritto")
    scores.sort(key=lambda score: score['baseScore'], reverse=True)
    #placeholder
    template = Template("""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
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
        </tr>
        {% for score in scores %}
           <tr>
            <td>{{ score.leaderboardPlayerInfo.name }}</td>
            <td>{{ score.baseScore }}</td>
            <td>{{ score.fullCombo }}</td>
          </tr>
          {% endfor %}
        </table>
      </body>
    </html>
    """)
    html = template.render(scores=scores)
    with open("index.html", "w", encoding="utf-16") as f:
     f.write(html)
    print("index.html scritto")
else:
    print("An error occurred:", response.status_code)
    print("mado rip lol")