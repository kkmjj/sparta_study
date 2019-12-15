import requests


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#1
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
music = soup.select('.newest-list > div > table > tbody > tr > td.info')


rank=1
for m in music: #td info 까지 적용 된 경로

    title = m.select_one('a.title').text
    star = m.select_one('a.artist').text

    doc = {                         #밖에 있는 for문에서 돌면서 저장
          'rank': rank,
         'title': title,
         'star': star
           }
    print(doc)
    db.music.insert_one(doc)    #mongo db 에  insert
    rank=rank+1


