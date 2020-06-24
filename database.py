import sqlite3

def dbcon(): 
    return sqlite3.connect('mydata.db')

#txtuser 테이블 생성
def create_usertable():
    try:
        query='''
        CREATE TABLE "txtuser"(
            "name" varchar(50),
            "hp" int default 100
        )
        '''
        db2 = dbcon()
        d = db2.cursor
        d.execute(query)
        db2.commit()
    except Exception as e:
        print('db2 error:', e)
    finally:
        db2.close()

#txtuser 데이터 입력
def insert_data2(name, hp): 
    try: 
        db2 = dbcon() 
        d = db2.cursor() 
        setdata = (name, hp) 
        d.execute("INSERT INTO users VALUES (?, ?)", setdata) 
        db2.commit() 
    except Exception as e: 
        print('db2 error:', e) 
    finally: 
        db2.close()

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
def select_id(id, pw): 
    ret = () 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (id, pw) 
        c.execute('SELECT * FROM users WHERE id = ? AND pw = ?', setdata) 
        ret = c.fetchone() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
    return ret

def check_id(id): 
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

def check_name(name): 
    ret = () 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (name) 
        c.execute('SELECT * FROM users WHERE name = ?', setdata) 
        ret = c.fetchone() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
    return ret

#create_table()
#insert_data('20191056', '2019', '윤현경')
#insert_data('id, 'pw', 'KIT')
#ret = select_all()
#ret = select_id('20191056')
#print(ret)