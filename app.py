from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/naver')
def naver():
    return '이페이지는 네이버입니다.'

@app.route('/winter')
def myimage():
    return render_template("myimage.html")


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        return "POST로 전달"

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)
