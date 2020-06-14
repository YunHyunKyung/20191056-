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
        return "GET으로 전달"
    else: 
        return "POST로 전달"

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
