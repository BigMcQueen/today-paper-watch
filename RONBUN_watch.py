import datetime
from bs4 import BeautifulSoup
import requests
# Import token saved in a separate file
import line_token

date_today = datetime.date.today()
target_url = f'https://aasj.jp/date/{date_today.year}/{date_today.month:02}/{date_today.day:02}'

r = requests.get(target_url)
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find('h2').get_text()

# The token is stored in 'token' in line_token.py
TOKEN = line_token.token

api_url = 'https://notify-api.line.me/api/notify'
send_contents = [title, target_url]

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

requests.post(api_url, headers=TOKEN_dic, data=send_dic)
