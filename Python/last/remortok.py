import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

ro_url = f"https://remoteok.io/remote-dev+python-jobs"

def extract_jobs(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    job_table = soup.find_all("tr", {"class": "job"})
    jobs = []
    for job in job_table:
        job_link = job["data-url"]
        job_title = job["data-search"]
        job_company = job["data-company"]
        result = {
            "title": job_title,
            "company": job_company,
            "link": f"https://remoteok.io{job_link}"
        }
        jobs.append(result)
    return jobs

def ro_jobs(lang):
    url = f"https://remoteok.io/remote-dev+{lang}-jobs"
    result = extract_jobs(url)
    return result