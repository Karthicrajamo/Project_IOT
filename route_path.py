from flask import Flask

app = Flask(__name__)
basepath = '/'

@app.route(basepath + '/base')
def base():
    return 'hello base'

if __name__ == '__main__':
    app.run()