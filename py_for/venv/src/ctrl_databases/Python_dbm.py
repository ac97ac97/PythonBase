import dbm
with dbm.open('mydb','c') as db:
    db['name'] = 'tony'     #更新数据
    print(db['name'].decode()) #取出数据

    age=int(db.get('age',b'18').decode())  #取出数据
    print(age)

    if 'age' in db:                 #判断是否存在age数据
        db['age'] ='20'             #或者 b'20'
    del db['name']                  #删除name数据