from flask import render_template,request
from DCapi import app

@app.route('/oauth',methods=['get','post'])
def indexOAUTH():
    return '22'
    #return render_template('test.html',url='/login',form=True)
