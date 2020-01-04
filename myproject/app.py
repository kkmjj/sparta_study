
#app.run('127.0.0.1',port=5000,debug=True)

from flask import Flask , render_template , jsonify ,request  # render_template 안에서 html 사용
import requests
from bs4 import BeautifulSoup

#엑셀 파일 생성 시 필요
from openpyxl import load_workbook



app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')



@app.route('/index.html')
def index():
   return render_template('index.html')

@app.route('/input.html')
def input():
   return render_template('input.html')

@app.route('/excel.html')
def excel():
   return render_template('excel.html')

@app.route('/entire.html')
def entire():
   return render_template('entire.html')


@app.route('/month.html')
def month():
   return render_template('month.html')




## API 역할을 하는 부분
@app.route('/money', methods=['POST'])
def saving():
   date = request.form['someDate_give']
   pay = request.form['money_give']
   cont = request.form['content_give']
   tag = request.form['tag_give']

   # 클라이언트로부터 데이터를 받는 부분

   # mongoDB에 넣는 부분

   imformation = {
      'somedate': date,
      'money':pay,
      'content':cont,
      'tag':tag,

   }

   db.counting.insert_one(imformation)


   return jsonify({'result': 'success'})




@app.route('/money', methods=['GET'])
def getting():
   # 모든 document 찾기 & _id 값은 출력에서 제외하기
  # result =list(db.counting.find({},{'_id':0}))
   result =list(db.counting.find({},{'_id':0}))
   # shops라는 키 값으로  내려주기
   return jsonify({'result': 'success', 'shops': result})

#엑셀 생성시
@app.route('/excel',methods=['GET'])
def exeting():
   result = list(db.counting.find({}, {'_id': 0}))
   row = 4
   work_book = load_workbook('prac01.xlsx')
   work_sheet = work_book['prac']
   sum=0
   cafe=0
   food=0
   medical=0
   other=0
   for s in result:
    print(s['somedate'])
    work_sheet.cell(row=row, column=1, value=s['somedate']) #날짜 엑셀에 적용
    work_sheet.cell(row=row, column=2, value=s['content'])  # 내용 엑셀에 적용
    work_sheet.cell(row=row, column=3, value=s['tag'])  # 태그 엑셀에 적용
    work_sheet.cell(row=row, column=4, value=s['money'])  #돈  엑셀에 적용
    sum+=int(s['money'])
    if(s['tag']=='카페'):
     cafe+=int(s['money'])
    if (s['tag'] == '카페'):
       cafe += int(s['money'])
    if (s['tag'] == '음식'):
       food += int(s['money'])
    if (s['tag'] == '의료비 및 보험비'):
       medical += int(s['money'])
    if (s['tag'] == '기타'):
       other += int(s['money'])
    row=row+1

   work_sheet.cell(row=4, column=6, value=sum)  # 총 금액 엑셀에 적용

    #태그별 금액
   work_sheet.cell(row=7, column=6, value=cafe)
   work_sheet.cell(row=7, column=7, value=food)
   work_sheet.cell(row=7, column=8, value=medical)
   work_sheet.cell(row=7, column=9, value=other)
   work_book.save('prac01.xlsx')

   return jsonify({'result': 'success', 'shops': result})


if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)