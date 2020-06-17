from flask import Flask, request, render_template, redirect, url_for
import txtgame
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/hello')
def hellohtml(): 
    return render_template("hello.html")

@app.route('/hello/<name>')
def hellovar(name):
    user = txtgame.set_user(name)
    return render_template('gamestart.html', data=user)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f: 
        data = f.read() 
        user = json.loads(data) 
    print(type(user)) 
    print(user)
    print(user['items'])
    return"{}이 {}을 사용했습니다.".format(user["name"], user["items"][0])

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

@app.route('/py')
def pyhtml():
    return render_template("py.html")

@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        # args_dict = request.args.to_dict() 
        # print(args_dict) 
        num = request.args["num"] 
        name = request.args.get("name") 
        return "GET으로 전달된 데이터({}, {})".format(num, name) 
        
    else: 
        num = request.form["num"] 
        name = request.form["name"] 
        with open("static/save.txt","w", encoding='utf-8') as f: 
            f.write("%s,%s" % (num, name)) 
        return "POST로 전달된 데이터({}, {})".format(num, name)

@app.route('/getinfo') 
def getinfo(): 
    # 파일 입력
    with open("static/save.txt", "r", encoding='utf-8') as file: 
        student = file.read().split(',') # 쉽표로 잘라서 student 에 배열로 저장 
        return '번호 : {}, 이름 : {}'.format(student[0], student[1])

if __name__ == '__main__': 
    with app.test_request_context(): 
        print(url_for('daum'))
    app.run(debug=True)
