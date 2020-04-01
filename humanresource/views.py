from flask import render_template,request
from humanresource.app import app
from humanresource.data.user import users

@app.route('/',methods=['get','post'])
def index():
    return render_template('test.html',url='/login',form=True)

@app.route('/login',methods=['get','post'])
def login():
    formdata=request.form.to_dict()
    if formdata in users['user']:
        return render_template('test.html',table=True)
    else:
        return False

@app.route('/main',methods=['get','post'])
def mainpage():
    return render_template('main.html')
@app.route('/test',methods=['get','post'])
def test():
    return render_template('testjinjia.html')
@app.route('/test01',methods=['get','post'])
def test01():
    return render_template('test01.html')

@app.route('/test02',methods=['get','post'])
def test02():
    return render_template('test02.html')