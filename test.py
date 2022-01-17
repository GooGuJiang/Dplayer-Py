from tkinter.messagebox import NO
from flask import Flask,render_template,send_from_directory,request
import re

def is_gu_url(url):
    if re.match(r'^https*://(pan.)*gmoe\.cc/', url) == None:
        return False
    else:
        return True


app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/play',methods=['GET','POST'])
def play_vidio():
    sp_url = request.args.get('spurl')
    sp_name = request.args.get('name')
    if sp_url == None:
        return "缺少参数spurl",404
    elif sp_name == None:
        return "缺少参数name",404

    if is_gu_url(sp_url) == False:
        return "抱歉，不支持该域名",500

    name=sp_name
    spurl=sp_url
    return render_template('splay.html',name=name,spurl=spurl)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
