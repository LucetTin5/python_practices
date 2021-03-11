from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file
app = Flask("Super")

db = {}


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/report")
def report():
    searching_job = request.args.get('word')
    if searching_job:
        searching_job = searching_job.lower()
        existingJobs = db.get(searching_job)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(searching_job)
            db[searching_job] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", 
        word=searching_job, 
        resultsNumbers=len(jobs),
        jobs = jobs
        )

@app.route("/export")
def export():
    try:
      searching_job = request.args.get('word')
      searching_job = searching_job.lower()
      if not searching_job:
        raise Exception()
      jobs = db.get(searching_job)
      if not jobs:
        raise Exception()
      save_to_file(jobs)
      return send_file("jobs.csv")
    except:
      return redirect("/")      

app.run(host="0.0.0.0")
