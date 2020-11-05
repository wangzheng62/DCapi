from flask import render_template,request
from DCapi import app
from DCapi.humanresource.data.user import users
#模板渲染偏函数，设置模板路径
dirnow='/humanresource'
def new_render_template(name,**content):
    return render_template(template_name_or_list=dirnow+name,**content)
#view定义
#测试页
@app.route('/test',methods=['get','post'])
def test():
    return new_render_template('/page/test.html',url='/login',form=True)
@app.route('/test01',methods=['get','post'])
def test01():
    return new_render_template('/test/starter.html',url='/login',form=True)
#主页
@app.route('/index',methods=['get','post'])
def index():
    return new_render_template('/page/index.html',url='/login',form=True)
#注册页
#
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

