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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num=0)

@app.route('/<int:num>s')
def seconds(num):
    return redirect(url_for('.index', num=num))


@app.route('/<int:num>m')
def minutes(num):
    return redirect(url_for('.index', num=num))


@app.route('/<int:num>h')
def hours(num):
    return redirect(url_for('.index', num=num))
