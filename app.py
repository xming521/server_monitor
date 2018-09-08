from flask import Flask

app = Flask(__name__)

# 写登录
@app.route('/')
def index():







    return 'Hello World!'


if __name__ == '__main__':
    app.run()
