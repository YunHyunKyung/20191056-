from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/hello')
def hellohtml(): 
    return render_template("hello.html")

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


@app.route('/move/naver') 
def naver(): 
    return redirect("https://www.naver.com/")

@app.route('/move/daum') 
def daum():
    return redirect("https://www.daum.net/")

if __name__ == '__main__': 
    with app.test_request_context(): 
        print(url_for('daum'))
    app.run(debug=True)