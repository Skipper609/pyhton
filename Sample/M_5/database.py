import json
data_lst = [
    {'id':1001,'wname':"Python",'year':2019,'status':1,'company':"Heraizen"},
    {'id':1002,'wname':"Javascript",'year':2018,'status':1,'company':"Spaneos"}
]

try:
    with open("db.json") as file:
        ws_list = json.load(file)
    print(ws_list)
        # for w in ws_list:
        #     print(f"Id :{w['id']}, Name : {w['wname']}, Year : {w['year']}")
except Exception as e:
    print(e)