
#app.run('127.0.0.1',port=5000,debug=True)

from flask import Flask , render_template , jsonify ,request  # render_template 안에서 html 사용
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.
## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
   id = request.form['name_give']
   area = request.form['address_give']
   cnt = request.form['count_give']
   number = request.form['phone_give']
   # 클라이언트로부터 데이터를 받는 부분

   # mongoDB에 넣는 부분

   imformation = {
      'name': id,
      'count':cnt,
      'address':area,
      'phone': number
   }

   db.shops.insert_one(imformation)


   return jsonify({'result': 'success'})




@app.route('/order', methods=['GET'])
def getting():
   # 모든 document 찾기 & _id 값은 출력에서 제외하기
   result =list(db.shops.find({},{'_id':0}))
   # articles라는 키 값으로 영화정보 내려주기
   return jsonify({'result': 'success', 'shops': result})



if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)