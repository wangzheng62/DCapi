from flask import Flask, redirect, render_template, request
from flask.views import View
from oauth import jsondata

app = Flask(__name__)
app.secret_key = 'some_secret'
@app.route('/',methods=['get'])
def mainpage():
    clientIP=request.remote_addr
    with app.test_client() as c:
        rv=c.get('/api/DB/em?host={}'.format(clientIP))
        res=rv.data.decode(encoding='utf8')
        print(type(res))
        print(res)
        re= jsondata.loads(res)
        print(re)

    if re['res']:
        return '快捷登录页面'
    else:
        return redirect('/loginfirst')

class LoginView(View):
    #methods = ['get']
    def __init__(self,**kw):
        self.kw=kw
    def dispatch_request(self,):
        return render_template('loginfirst.html', **self.kw)
view=LoginView.as_view('loginfirst',url='/api/DB/em')
app.add_url_rule('/loginfirst',view_func=view)

@app.route('/test',methods=['get'])
def test():
    return render_template('test.html')