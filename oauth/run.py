
from oauth.loginhistoru import app

if __name__ == '__main__':
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.run(host='0.0.0.0', debug=True)