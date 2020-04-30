import requests
from bs4 import BeautifulSoup

login_url = 'https://everytime.kr/user/login'
craw_url = 'https://everytime.kr/timetable'

session = requests.session()

params = dict()
params['m_id'] = 'jiyoung15105'
params['m_passwd'] = 'dlatnrud105'

res = session.post(login_url, data = params)
res.raise_for_status()

print(res.headers)
print(session.cookies.get_dict())

res = session.get(craw_url)
soup = BeautifulSoup(res.content,'html.parser')
numbers = soup.select('.list table tbody tr')
for number in numbers:
    title = number[10].text
    print(title)
