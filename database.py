import sqlite3

def dbcon(): 
    return sqlite3.connect('mydata.db')

#users 테이블 생성 함수
def create_table(): 
    try:
        query = '''
        CREATE TABLE "users"(
            "id" varchar(50),
            "pw" varchar(50),
            "name" varchar(50),
            PRIMARY KEY("id")
            )
        '''
        db = dbcon() 
        c = db.cursor() 
        c.execute(query)
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally:
        db.close()

# 데이터 입력 함수
def insert_data(id, pw, name): 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (id, pw, name) 
        c.execute("INSERT INTO users VALUES (?, ?, ?)", setdata) 
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close()

#전체 데이터를 갖고 오는 함수
def select_all(): 
    ret = list() 
    try:
        db = dbcon() 
        c = db.cursor() 
        c.execute('SELECT * FROM users') 
        ret = c.fetchall()
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
    return ret

#아이디로 데이터 검색하는 함수
def select_id(id): 
    ret = () 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (id,) 
        c.execute('SELECT * FROM users WHERE id = ?', setdata) 
        ret = c.fetchone() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
    return ret

#create_table()
#insert_data('20191056', '2019', '윤현경')
#ret = select_all()
#ret = select_id('20191056')
#print(ret)