import requests
import os
from scrapper import get_story, make_info, make_detail_url
from flask import Flask, render_template, request

os.system("cls")

db = {}
app = Flask("HN_Clone")


@app.route("/")
def home():
    # 첫 페이지는 popular가 메인
    data_list = get_story(popular)
    return render_template("index.html", data_list=data_list)


@app.route("/")


app.run(host="127.0.0.1")
