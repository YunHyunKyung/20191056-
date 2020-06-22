from flask import Flask, request, render_template, redirect, url_for, session
import txtgame
import json
import database 
app = Flask(__name__)
app.secret_key = b'aaa!111/'

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
            return "아이디 또는 패스워드를 확인 하세요." 
            
# 로그아웃(session 제거) 
@app.route('/logout') 
def logout(): 
    session.pop('users', None) 
    return ''' 
        <script> alert("로그아웃 되었습니다."); 
        location.href="/login" 
        </script>''' 
    
# 로그인 사용자만 접근 가능으로 만들면 
#@app.route('/form') 
#def form(): 
#    if 'users' in session: 
#        return render_template('getinfo.html') 
#    return redirect(url_for('login'))

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


#값 입력받기, 저장하기
#@app.route('/method', methods=['GET', 'POST']) 
#def method(): 
#    if request.method == 'GET': 
#        # args_dict = request.args.to_dict() 
#        # print(args_dict) 
#        id = request.args["id"]
#        pw = request.args["pw"] 
#        name = request.args.get("name") 
#        return "GET으로 전달된 데이터({}, {}, {})".format(id, pw, name) 
#        
#    else: 
#        id = request.form["id"]
#        pw = request.form["pw"] 
#        name = request.form["name"] 
#        #with open("static/save.txt","w", encoding='utf-8') as f: 
#        #    f.write("%s,%s,%s" % (id, pw, name)) 
#        database.insert_data(id, pw, name)
#        return "POST로 전달된 데이터. 아이디 : {}, 비밀번호 : {} 이름 : {}".format(id, pw, name)

#입력받은 값 출력하기
#@app.route('/getinfo') 
#def getinfo(): 
    # 파일 입력
    #with open("static/save.txt", "r", encoding='utf-8') as file: 
    #    student = file.read().split(',') # 쉼표로 잘라서 student 에 배열로 저장 
#    ret = database.select_all()
#    print(ret)
#    return render_template('getinfo.html', data=ret)
    #return '아이디 : {}, 비밀번호 : {} 이름 : {}'.format(users[0], users[1], users[2])

#txt게임
@app.route('/gamestart', methods=['GET', 'POST'])
def gamestart():
    if 'users' in session: 
        if request.method == 'GET': 
            return render_template('gamestart.html') 
        else: 
            name = request.form['name']
            ret = database.check_name(name)
            if ret != None:
                user = txtgame.set_user(ret[2])
                return render_template('game.html', data=user)
            else: 
                return "회원가입 시 사용한 이름을 입력하시오."
    else:
        return ''' 
            <script> alert("로그인 후 이용하세요"); 
            location.href="/login" 
            </script>'''

@app.route('/game') 
def game(): 
    return render_template('game.html')

#@app.route('/gamestart')
#def gamestart():
#    with open("static/save.txt", "r", encoding='utf-8') as f: 
#        data = f.read() 
#        user = json.loads(data) 
#    print(type(user)) 
#    print(user)
#    print(user['items'])
#    return"{}이 {}을 사용했습니다.".format(user["name"], user["items"][0])

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "당신은 이수만의 ATM이 되었습니다. HP -5"
    elif num == 2:
        return "당신은 경찰서로 소환되었습니다. HP -50"
    elif num == 3:
        return "당신은 아무런 타격도 입지 않았습니다. HP -0"
    elif num == 4:
        with open("static/save.txt", "r", encoding='utf-8') as f: 
            data = f.read() 
            user = json.loads(data) 
            print(user['items'])
        return"{}이 {}을 사용했습니다.".format(user["name"], user["items"][0])


if __name__ == '__main__': 
#    with app.test_request_context(): 
#        print(url_for('daum'))
    app.run(debug=True)