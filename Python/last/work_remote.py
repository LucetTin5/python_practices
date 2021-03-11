import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

def get_categories(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    containers = soup.find("div", {"class": "jobs-container"}).find_all("section", {"class": "jobs"})
    categories = []
    for section in containers:
        category_info = section.find("h2").find("a")
        category_title = category_info.string.strip()
        category_link = category_info["href"]
        category_page = f"https://weworkremotely.com{category_link}"

        categories.append({
            "title": category_title,
            "link": category_page
        })
    return categories


def extract_jobs(category_link):
    result = requests.get(category_link)
    soup = BeautifulSoup(result.text, "html.parser")
    job_list = soup.find("div", {"class":"content"}).find("ul").find_all("li")[1:-1]
    jobs = []
    for job in job_list:
        if job.find("div", {"class": 'highlight-bar'}):
            pass
        else:
            job_info = job.find("a")
            job_link = job_info["href"]
            job_company = job_info.find("span", {"class": "company"}).string
            job_title = job_info.find("span", {"class": "title"}).string
            job_ = {
                "title": job_title,
                "company": job_company,
                "link": f"https://weworkremotely.com{job_link}"
            }
            jobs.append(job_)
    return jobs


def wr_jobs(lang):
    url = f"https://weworkremotely.com/remote-jobs/search?term={lang}"
    categories = get_categories(url)
    pages = []
    for category in categories:
        pages.append(category["link"])
    jobs = []
    for page in pages:
        print(f"Scrapping ro page: {page}")
        jobs += extract_jobs(page)
    return jobs

