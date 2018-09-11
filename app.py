import logging

from flask import Flask, request, flash, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

import monitor

app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'some_secret'

# 解决缓存刷新问题
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=2)


logging.getLogger('werkzeug').setLevel(logging.ERROR)
handler = logging.FileHandler(filename='log.txt', mode='a')
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)


# 错误处理
@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return flash('出现错误')


# 继承用户类
class User(UserMixin):
    pass


# 创建登录用户
@login_manager.user_loader
def load_user(stu_id):
    curr_user = User()
    curr_user.id = stu_id
    return curr_user


# 主页
@app.route('/')
@login_required
def index():
    result = monitor.main()
    print(result)
    return render_template('index.html', dict=result)


# 未登录的强制登录
@login_manager.unauthorized_handler
def force_login():
    return render_template('login.html')


# 登录
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        # 验证表单中提交的用户名和密码
        if name == 'admin' and password == 'zym233521':
            curr_user = User()
            curr_user.id = name
            # 通过Flask-Login的login_user方法登录用户  remember=True记住登录
            login_user(curr_user, remember=True)
        else:
            return render_template('login.html', error="1")
    return redirect(url_for('index'))


# 登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
