from flask import Flask, render_template, request, redirect, session
from controller.JobController import jobController
from controller.StockController import stockController
import json


app = Flask(__name__)  # Flask对象

app.config['SECRET_KEY'] = "AIWORKPROJECT123456789"  # 使用session必须配置
app.register_blueprint(jobController)
app.register_blueprint(stockController)

@app.route('/')        # 装饰器 类似 Java的注解   route路由flask中 绑定url和处理函数之间的对应关系
def index():
    return render_template("index.html")

@app.route('/gologin')
def goLogin():
    return render_template('login.html')

# error 
@app.errorhandler(404)
def handle_bad_request(error):
    return redirect('/goerror')  # 重定向到指定的网页

# 404 page
@app.route('/goerror')
def error_page():
    return render_template('ui-404.html')

@app.route('/login', methods=['POST'])
def login():
    userName = request.form.get('userName')
    userPassword = request.form.get('userPassword')
    if userName == 'zhangsan' and userPassword == '123456': # 模拟登录
        session['user'] = userName
        return render_template('index.html')
    return render_template('login.html')

@app.route('/dashboard')
def goDashboard():
   return render_template('index-crypto-dashboard.html')

@app.route('/visualize')
def visualize():
    return render_template('echarts.html')

@app.route('/timeline')
def tileline():
    return render_template('echarts.html')

@app.route('/charts-echart-line')
def line():
    return render_template('charts-echart-line.html')

@app.route('/charts-echart-bar')
def bar():
    return render_template('charts-echart-bar.html')

@app.route('/basicstock')
def basicstock():
    return render_template('basic-stock.html')

@app.route('/newpage')
def newpage():
    return render_template('new_page.html')

@app.route('/stockdetailspage')
def stockdetailspage():
    return render_template('stock-details.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)          # 会启动Web应用服务，默认端口号是5000

