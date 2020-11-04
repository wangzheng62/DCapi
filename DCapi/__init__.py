#import os,sys
#pwd=os.getcwd()
#sys.path.append(pwd)
from flask import Flask
app = Flask(__name__)
app.secret_key = 'some_secret'
import DCapi.humanresource.views
import DCapi.humanresource.api
import DCapi.oauth.views
