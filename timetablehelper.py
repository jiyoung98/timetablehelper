from flask import Flask, render_template, jsonify, request
app = Flask(__name__)



from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


import requests


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/schedules')
# def schedule_list():
#     code1 = ['s1100100H1', 's1100200H1', 's1100250H1', 's1100300H1', 's1100400H1', 's1100500H1', 's1101000H1',
#              's1102000H1', 's1102100H1', 's1103000H1', 's1104000H1', 's1105000H1', 's1106000H1', 's1107000H1',
#              's1109000H1', 's1110000H1', 's1111000H1', 's1125000H1', 's1135000H1', 's1143000H1', 's1145000H1',
#              's1150000H1', 's1155000H1', 's1169000H1', 's1170000H1', 's1171000H7', 's1172000H8', 's1173000H9',
#              's1174000H1', 's1180000H1']
#
#     data4 = []
#
#     db.schedulelist.remove({});
#
#     for i in code1:
#         headers = {'Referer': 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_new.jsp'}
#         data = requests.get(
#         'http://ysweb.yonsei.ac.kr:8888/DataAgent?pgm=/curri120601/curri_Data&DmlGb=get_list&ocode0=s1&ocode1='+i+'&s2=all&schHakjum=all&hy=2020&hg=1&lang=0&filterscount=0&groupscount=0&pagenum=0&pagesize=15&recordstartindex=0&recordendindex=32.64&_=1586437431115',
#         headers=headers)
#
#         data2 = data.json()['Data']
#
#         data3 = []
#
#         for j in data2:
#             kna = j['KNA']
#             hakbb = j['HAKBB']
#             hakjum = j['HAKJUM']
#             oname2 = j['ONAME2']
#             prof = j['PROF']
#             room = j['ROOM']
#             time = j['TIME']
#             notice = j['GUBUN']
#             ocode1 = j['OCODE1']
#
#             doc = {"kna": kna, "hakbb": hakbb, "hakjum": hakjum, "oname2": oname2, "prof": prof, "room": room, "time": time, "notice": notice, "ocode1": ocode1}
#
#             db.schedulelist.insert(doc)
#
#             data3.append(doc)
#
#         data4.append(data3)
#
#     return jsonify(data4)


## API 역할을 하는 부분
@app.route('/schedules', methods=['GET'])
def read_schedules():
    schedules = list(db.schedulelist.find({},{'_id':0}))
    return jsonify({'result': 'success', 'schedules': schedules})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

