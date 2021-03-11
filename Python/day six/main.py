import os
import csv
import requests
from bs4 import BeautifulSoup as bs


os.system("cls")
alba_url = "http://www.alba.co.kr"
html = requests.get(alba_url)
soup = bs(html.text, "html.parser")

companys = []

def get_super_companys(soup):
    supers = soup.find("div", {"id": "MainSuperBrand"}).find_all("li", {"class": "first impact", "class": "impact"})
    links = []
    for li in supers:
        link = li.find("a")["href"]
        company = li.find("span", {"class": "company"}).string
        links.append((link, company))
    return links

super_link_company = get_super_companys(soup)


def get_jobs_data(li):
    # for i in range(len(li)):
    company_link = li[1][0]
    company_page = requests.get(company_link)
    company_soup = bs(company_page.text, "html.parser")
    job_table = company_soup.find("div", {"id": "NormalInfo"}).find("table").find("tbody").find_all("tr")
    print(type(set(job_table)))
    
    # jobs = []
    # for tr in job_table:
    #     place = tr.find("td", {"class": "local"}).get_text()
    #     place = place.replace("\xa0", " ")
    #     title = tr.find("td", {"class": "title"}).find("span", {"class": "company"}).string
    #     time = tr.find("td", {"class": "data"}).string
    #     pay = tr.find("td", {"class": "pay"}).find_all("span")
    #     payment = pay[0].string + pay[1].string
    #     date = tr.find("td", {"class": "regDate last"}).string
    #     job_list = (place, title, time, payment, date)
    #     jobs.append(job_list)
    # return jobs

get_jobs_data(super_link_company)

# def make_file(data):
#     for company in super_link_company:
#         file = open(f"{super_link_company[1]}.csv", mode="w", encoding="utf-8-sig")
#         writer = csv.writer(file)
#         writer.writerow(["place", "title", "time", "pay", "date"])
#         # 이 다음은 각 링크에서 뽑아낸 데이터를 입력
#         for datum in data:
#             writer.writerow(datum)

# def get_job(soup):
#     table = soup.find("div", {"id": "NormalInfo"}).find("table").find("tbody").find_all("tr", {"class": "", "class": "divide"})
#     job_count = int(soup.find("p", {"class": "jobCount"}).find("strong").string)
#     job_list = []
#     for i in range(job_count):
#         place = table[i].find("td", {"class": "local first"}).string
#         title = table[i].find("td", {"class": "title"}).find("span", {"class": "company"}).string
#         time = table[i].find("td", {"class": "data"}).string
#         pay = table[i].find("td", {"class": "pay"}).string
#         date = table[i].find("td", {"class": "regDate last"}).string
#         job_list.append((place, title, time, pay, date))
#     return job_list
    

# data = get_jobs_data(super_link_company)
# print(data)




