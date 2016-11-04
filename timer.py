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
from time import sleep
from flask import Flask, render_template, flash, url_for

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')


@app.route('/<int:num>s')
def seconds(num):
    sleep(num)
    return render_template('over.html')


@app.route('/<int:num>m')
def minutes(num):
    sleep(num*60)
    return render_template('over.html')


@app.route('/<int:num>h')
def hours(num):
    sleep(num*3600)
    return render_template('over.html')
