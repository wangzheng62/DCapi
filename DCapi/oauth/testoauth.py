from flask import Flask, jsonify,url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id='{{ your-github-client-id }}',
    client_secret='{{ your-github-client-secret }}',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = github.authorize_access_token()
    # you can save the token into database
    profile = github.get('/user')
    return jsonify(profile)

if __name__=='__main__':
    app.run('127.0.0.1',port=6500)