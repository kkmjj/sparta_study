import requests


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#1
data = requests.get('http://spartacodingclub.shop/post',headers=headers)
rjson = data.json()
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦


#2
for i in rjson['articles']:

    doc ={
        'comment': i['comment'],
        'desc': i['desc'],
        'image': i['image'],
        'title': i['title'],
        'url': i['url']
    }
#3
    db.ap.insert_one(doc)

#4
    target = list(db.ap.find({}))
    for i in target:
        print(i)


