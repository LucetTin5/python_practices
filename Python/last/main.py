import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, redirect, render_template
from remortok import ro_jobs
from stackoverflow import get_so as so_jobs
from work_remote import wr_jobs


os.system("cls")

app = Flask.app("remote_job")

@app.route("/")
def home():
    render_template("home.html")

@app.route("/read")
def read():
    language = request.args("lang")
    jobs = ro_jobs(language) + so_jobs(language) + wr_jobs(language)

    render_template("read.html", jobs=jobs)


app.run(host="127.0.0.1")