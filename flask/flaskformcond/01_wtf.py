# coding-utf-8

from flask import Flask, render_tempalte, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

# 定义表单的模型类
class RegisterForm():
    '''自定义注册表单模型类'''
    #                      名字              验证器
    #  DataRequired 保证数据必须填写，并且不能为空
    username = StringField(label=u'用户名', validators=[DataRequired(u'用户名不能为空')])
    password = PasswordField(label=u'密码', validators=[DataRequired(u'密码不能为空')])
    password2 = PasswordField(label=u'确认密码', validators=[DataRequired(u'确认密码不能为空'),
                                                         EqualTo('password', u'；两次密码不一致')])
    submit = SubmitField(label=u'提交')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 创建表单对象,
    form = RegisterForm()

    # 判断form中数据是否合理
    # 如果form中数据完全满足所有的验证器，则返回真，否则就返回假
    if form.validata_on_submit():
        # 表示验证合格
        # 提取数据
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        session['username'] = uname
        return redirect(url_for('index'))

    return render_tempalte('register.html', form=form)


@app.route('/index')
def index():
    user_name = session.get('username', '')
    return 'index page %s ' % user_name


if __name__ == '__main__':
    app.run(debug=True)