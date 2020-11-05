from DCapi import app
if __name__=='__main__':
    print(app.static_url_path)
    print(app.static_folder)
    print(app.config)
    app.run('0.0.0.0',port=8898,debug=True)