from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/move/naver') 
def naver(): 
    return redirect("https://www.naver.com/")

@app.route('/move/daum') 
def daum():
    return redirect("https://www.daum.net/")

@app.route('/urltest1') 
def url_test1(): 
    return redirect(url_for('naver'))

@app.route('/urltest2') 
def url_test2(): 
    return redirect(url_for('daum'))

if __name__ == '__main__': 
    with app.test_request_context(): 
        print(url_for('daum'))
        print(url_for('naver'))
    app.run(debug=True)
