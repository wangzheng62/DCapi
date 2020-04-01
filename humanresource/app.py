from flask import Flask
import os
pwd=os.getcwd()
app = Flask(__name__,static_folder=pwd+r'\static\AdminLTE',static_url_path='')
app.secret_key = 'some_secret'
