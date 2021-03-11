import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

# Python search
so_url = f"https://stackoverflow.com/jobs?r=true&q=python"

def get_last_so(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser") 
    pagination = soup.find("div", {"class": "s-pagination"}).find_all("a", {"class": "s-pagination--item"})
    last_page = pagination[-2].get_text().strip()
    return int(last_page)


def get_jobs_so(soup):
    jobs = soup.find_all("div", {"class": "js-result"})
    so_list = []
    for job in jobs:
        job_title = job.find("h2").find("a", {"class": "s-link"})["title"]
        job_company = job.find("h3").find("span").get_text().strip()
        job_id = job["data-jobid"]
        job_link = f"https://stackoverflow.com/jobs?id={job_id}"
        so_list.append({
            "title": job_title,
            "company": job_company,
            "link": job_link
        })
    return so_list

def so_jobs(last_page):
    pages = range(1, last_page + 1)
    jobs = []
    for page in pages:
        print(f"Scrapping SO pages: {page}")
        page_url = so_url + f"&pg={page}"
        so_page = requests.get(page_url)
        so_soup = BeautifulSoup(so_page.text, "html.parser")
        job_in_page = get_jobs_so(so_soup)
        jobs += job_in_page
    return jobs

def get_so(lang):
    so_url = f"https://stackoverflow.com/jobs?r=true&q={lang}"
    last_page = get_last_so(so_url)
    so_list = so_jobs(last_page)
    return so_list

