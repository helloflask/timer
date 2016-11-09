# -*- coding: utf-8 -*-
"""
author: Grey Li
blog: withlihui.com
email: withlihui@gmail.com
github: github.com/greyli
column: zhuanlan.zhihu.com/flask
---------------------------------
A simple timer made with Flask and JavaScript.
https://github.com/helloflask/timer-flask
---------------------------------
MIT license.
"""
import re
from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very secret string'


@app.route('/')
def index():
    return redirect(url_for('timer', num=11*60+11))


@app.route('/<int:num>s')
@app.route('/<int:num>')
def timer(num):
    return render_template('index.html', num=num)


@app.route('/custom', methods=['GET', 'POST'])
def custom():
    time = request.form.get('time', 180)
    # use re to validate input data
    m = re.match('\d+[smh]?$', time)
    if m is None:
        flash(u'请输入一个有效的时间，例如34、20s、15m、2h')
        return redirect(url_for('index'))
    if time[-1] not in 'smh':
        return redirect(url_for('timer', num=int(time)))
    else:
        type = {'s': 'timer', 'm': 'minutes', 'h': 'hours'}
        return redirect(url_for(type[time[-1]], num=int(time[:-1])))


@app.route('/<int:num>m')
def minutes(num):
    return redirect(url_for('timer', num=num*60))


@app.route('/<int:num>h')
def hours(num):
    return redirect(url_for('timer', num=num*3600))

# todo pomodoro mode: loop a 25-5 minutes cycle
@app.route('/pomodoro')
def pomodoro():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_fouond(e):
    flash(u'访问地址出错了，鼠标放在问号上了解更多: )')
    return redirect(url_for('timer', num=244))
