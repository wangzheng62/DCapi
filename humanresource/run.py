from humanresource.app import app
import humanresource.views
import humanresource.api
if __name__=='__main__':
    print(app.static_url_path)
    print(app.static_folder)
    app.run('0.0.0.0',port=8888,debug=True)