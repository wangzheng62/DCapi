from flask_restful import Resource,Api
from flask import request
import json,os
from DCapi import app

api=Api(app,prefix='/api/humanresource')
class JSONdata(Resource):
    def get(self,filename):
        pwd=os.getcwd()
        print(pwd)
        with open(pwd+'/data/{}.json'.format(filename),'r') as f:
            return json.load(f)
    def post(self,filename):
        formdata=request.form.to_dict()
        print(formdata)
        print(filename)
        pwd=os.getcwd()
        print(pwd)
        with open(pwd+'/data/{}.json'.format(filename),'a') as f:
            f.close()
        return True
    def put(self,filename):
        formdata=request.form.to_dict()
        print(formdata)
        print(filename)
        pwd=os.getcwd()
        print("put")
        with open(pwd+'/data/{}.json'.format(filename),'a') as f:
            f.close()
        return True
    def delete(self,filename):
        formdata=request.form.to_dict()
        print(formdata)
        print(filename)
        pwd=os.getcwd()
        print("del")
        with open(pwd+'/data/{}.json'.format(filename),'a') as f:
            f.close()
        return True



api.add_resource(JSONdata,'/jsondata/<filename>')

class PYdata(Resource):
    def get(self,dictname):

        return eval('humanresource.data.user.{}'.format(dictname))
    def post(self):
        formdata=request.form.to_dict()


        return True
    def put(self):
        return True
    def delete(self):
        return True
api.add_resource(PYdata,'/pydata/<dictname>')
#错误示范
from flask import render_template,make_response
class Html(Resource):
    def get(self,filename):
        return make_response(render_template(filename))


api.add_resource(Html, '/html/<filename>')