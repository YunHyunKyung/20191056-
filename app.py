from flask import Flask, request, render_template, redirect, url_for, session
import txtgame
import json
import database 
import glob
app = Flask(__name__)
app.secret_key = b'aaa!111/'
hp = 100
gname =""
result1 = 0

#시작 화면
@app.route('/')
def hello():
    return render_template('hello.html')

#회원 가입
@app.route('/join', methods=['GET', 'POST']) 
def join(): 
    if request.method == 'GET': 
        return render_template('join.html') 
    else: 
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        ret = database.check_id(id)
        if ret == None: 
            database.insert_data(id, pw, name)
            return ''' 
            <script> alert("안녕하세요, {}님. 가입을 환영합니다."); 
            location.href='/login';
            </script> '''.format(name)
        else: 
            return ''' 
            <script> alert("중복된 아이디입니다."); 
            location.href='/join';
            </script> '''

#로그인
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'GET': 
        return render_template('login.html') 
    else: 
        id = request.form['id']
        pw = request.form['pw']
         # id와 pw가 db 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다 
        ret = database.select_id(id, pw)
        print(ret[2])
        if ret != None: 
            session['users'] = id
            return ''' 
            <script> alert("안녕하세요~ {}님"); 
            location.href="/getinfo" 
            </script> '''.format(ret[2])
        else: 
            return '''
            <script> alert("아이디 또는 패스워드를 확인 하세요.");
            location.href="/login"
            </script>'''
            
# 로그아웃(session 제거) 
@app.route('/logout') 
def logout(): 
    session.pop('users', None) 
    return ''' 
        <script> alert("로그아웃 되었습니다."); 
        location.href="/login" 
        </script>''' 

@app.route('/getinfo') 
def getinfo(): 
    if 'users' in session:
        ret = database.select_all()
        print(ret)
        return render_template('getinfo.html', data=ret)
    return ''' 
        <script> alert("로그인 후 이용하세요"); 
        location.href="/login" 
        </script>'''

#txt게임
@app.route('/gamestart', methods=['GET', 'POST'])
def gamestart():
    if 'users' in session: 
        if request.method == 'GET': 
            return render_template('gamestart.html') 
        else: 
            name = request.form["name"]
            user = txtgame.set_user(name)
            #session['user'] = user
            global gname
            gname = name
            return render_template('game.html', data=user)
    else:
        return ''' 
            <script> alert("로그인 후 이용하세요"); 
            location.href="/login" 
            </script>'''

@app.route('/game') 
def game(): 
    return render_template('game.html')

@app.route('/input/<int:num>')
def input_num(num):
    global hp
    if num == 1:
        hp = hp-5
        return ''' 
        <script> alert("당신은 이수만의 ATM이 되었습니다. HP -5");
        location.href="/game2"
        </script>'''
    elif num == 2:
        hp = hp-50
        return ''' 
        <script> alert("당신은 경찰서로 소환되었습니다. HP -50"); 
        location.href="/game2" 
        </script>'''
    elif num == 3:
        hp = hp-0
        return '''
        <script> alert("당신은 아무런 타격도 입지 않았습니다. HP -0"); 
        location.href="/game2" 
        </script>'''
    elif num == 4:
        return redirect(url_for('game11'))

@app.route('/game11')
def game11():
    global gname,hp
    user = { "name" : gname , "hp" : hp }
    return render_template('game1-1.html',data = user)

@app.route('/input10/<int:num10>')
def input10_num(num10):
    global hp
    if num10 == 1:
        hp = hp-0
        return ''' 
        <script> alert("이수만에게 피해를 입혔습니다. 이수만 처치");
        location.href="/game2"
        </script>'''
    elif num10 == 2:
        hp = hp-10
        return ''' 
        <script> alert("이수만에게 역습당했습니다. HP -10"); 
        location.href="/game2" 
        </script>'''
    elif num10 == 3:
        hp = hp-0
        return '''
        <script> alert("이수만을 치료합니다. HP -0"); 
        location.href="/game2" 
        </script>'''

@app.route('/game2') 
def game2(): 
    global gname,hp
    user = { "name" : gname , "hp" : hp }
    return render_template('game2.html',data = user)

@app.route('/input2/<int:num2>')
def input2_num(num2):
    global hp
    if num2 == 1:
        hp = hp+120408
        return ''' 
        <script> alert("당신은 엑소의 팬이 되었습니다. HP +120408"); 
        location.href="/game3" 
        </script>'''
    elif num2 == 2:
        hp = hp -120408
        return ''' 
        <script> alert("사형. HP -120408"); 
        location.href="/game3" 
        </script>'''
    elif num2 == 3:
        hp = hp -100
        return '''
        <script> alert("바보같은 선택을 하였습니다. HP -100"); 
        location.href="/game3" 
        </script>'''
    elif num2 == 4:
        return redirect(url_for('game12'))

@app.route('/game12')
def game12():
    global gname,hp
    user = { "name" : gname , "hp" : hp }
    return render_template('game2-1.html',data = user)

@app.route('/input11/<int:num11>')
def input11_num(num11):
    global hp
    if num11 == 1:
        hp = hp+100
        return ''' 
        <script> alert("엑소를 응원합니다. HP +100");
        location.href="/game3"
        </script>'''
    elif num11 == 2:
        hp = hp+1000
        return ''' 
        <script> alert("엑소에게 몬스터 춤을 보여줍니다. HP +1000"); 
        location.href="/game3" 
        </script>'''
    elif num11 == 3:
        hp = hp+10000
        return '''
        <script> alert("엑소에게 파워를 불러줍니다. HP +10000"); 
        location.href="/game3" 
        </script>'''

@app.route('/game3') 
def game3(): 
    global gname,hp
    user = { "name" : gname , "hp" : hp }
    return render_template('game3.html', data = user)

@app.route('/input3/<int:num3>')
def input3_num(num3):
    global hp
    if num3 == 1:
        hp = hp -500
        return ''' 
        <script> alert("적이 생겼습니다. HP -500"); 
        location.href="/result" 
        </script>'''
    elif num3 == 2:
        hp = hp +120408
        return ''' 
        <script> alert("동료가 생겼습니다. HP +120408"); 
        location.href="/result" 
        </script>'''
    elif num3 == 3:
        hp = hp -100
        return '''
        <script> alert("바보같은 선택을 하였습니다. HP -100"); 
        location.href="/result"
        </script>'''

#게임 결과
@app.route('/result', methods=['GET', 'POST'])
def result():
    global gname,hp,result1
    if(hp>10000):
        result1 = 1
        return render_template('gameresult.html', result1 = result1)
    if(0<hp<10000):
        result1 = 2
        return render_template('gameresult.html', result1 = result1)
    if(hp<=0):
        result1 = 3
        return render_template('gameresult.html', result1 = result1)

if __name__ == '__main__': 
    app.run(debug=True)