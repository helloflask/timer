# -*- coding: utf-8 -*-
"""
author: Grey Li
blog: greyli.com
email: withlihui@gmail.com
github: github.com/greyli
column: zhuanlan.zhihu.com/flask
---------------------------------
A simple timer made with Flask and JavaScript.
https://github.com/helloflask/timer-flask
---------------------------------
MIT license.
"""
from flask import Flask, render_template, url_for, redirect
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very secret string'

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('timer', num=180))


@app.route('/<int:num>s', methods=['GET', 'POST'])
@app.route('/<int:num>', methods=['GET', 'POST'])
def timer(num):
    form = TimeForm()
    if form.validate_on_submit():
        time = form.time.data
        if time[-1] not in 'smh':
            return redirect(url_for('timer', num=time))
        else:
            type = {'s': 'timer', 'm': 'minutes', 'h': 'hours'}
            return redirect(url_for(type[time[-1]], num=time[:-1]))
    return render_template('index.html', form=form, num=num)


@app.route('/<int:num>m', methods=['GET', 'POST'])
def minutes(num):
    return redirect(url_for('timer', num=num*60))


@app.route('/<int:num>h', methods=['GET', 'POST'])
def hours(num):
    return redirect(url_for('timer', num=num*3600))

# todo pomodoro mode: loop a 25-5 minutes cycle
@app.route('/pomodoro')
def pomodoro():
    return render_template('index.html')

class TimeForm(Form):
    time = StringField()
    submit = SubmitField(u'提交')

    def validate_time(self, field):
        if field.data not in 'smh0123456789':
            raise ValidationError(u'请输入一个有效的时间，参见帮助')