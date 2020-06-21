import sqlite3 
conn = sqlite3.connect('mydata.db') 

# Cursor 객체 생성 
c = conn.cursor() 

# 테이블 생성 
# c.execute("CREATE TABLE students (num varchar(50), name varchar(50))") 

# 데이터 삽입 
# c.execute("INSERT INTO students VALUES ('20201234', '파이썬')")

# execute 에 db 에 적용 
# conn.commit() 

# 데이터 불러 와서 출력
for row in c.execute('SELECT * FROM students'): 
    print(row)

# 접속한 db 닫기 
conn.close()