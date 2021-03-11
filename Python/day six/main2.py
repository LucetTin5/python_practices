import os
import csv
import requests as rq
from bs4 import BeautifulSoup as bs

os.system("cls")
alba_url = "http://www.alba.co.kr"

html_data = rq.get(alba_url)
soup = bs(html_data.text, "html.parser")

# 수프 -> 슈퍼브랜드 링크


def super_link(soup):
    sup = soup.find("div", {"id": "MainSuperBrand"}).find(
        "ul", {"class": "goodsBox"})
    link_all = sup.find_all("li")
    super_link = []
    super_company = []
    for data in link_all:
        link = data.find("a", {"class": "brandHover"})["href"]
        company = data.find("a", {"class": "brandHover"}).find(
            "strong").get_text()
        super_link.append(link)
        super_company.append(company)
    return super_link, super_company


# 한 페이지에서 일들을 리스트로 추출
def get_page_info(page_url):
    a = page_url
    job_list = rq.get(a)
    sup = bs(job_list.text, "html.parser")
    alba_table = list(
        sup.find("div", {"id": "NormalInfo"}).find("tbody").find_all("tr"))
    # 한 페이지에서 알바 정보들을 리스트에 담는다.
    alba_infos = []
    for i in range(len(alba_table)//2 - 1):
        alba_infos.append(alba_table[2 * i])
    return alba_infos

# 각 정보의 내부 정보들을 추출한다.


def get_alba_info(infos):
    alba_info = []
    for info in infos:
        information = info
        place = information.find("td", {"class": "local"})
        if place:
            place = place.get_text().replace("\xa0", " ")
        else:
            place = ""
        title = information.find("td", {"class": "title"}).find(
            "span", {"class": "company"})
        if title:
            title = title.string
        else:
            title = ""
        time = information.find("td", {"class": "data"}).find(
            "span", {"class": "time"})
        if time:
            time = time.get_text()
        else:
            time = ""
        payment = information.find("td", {"class": "pay"}).find_all("span")
        if payment:
            pay = payment[0].string + " " + payment[1].string
        else:
            pay = ""
        date = information.find("td", {"class": "regDate"})
        if date:
            date = date.get_text()
        else:
            date = ""
        data = (place, title, time, pay, date)
        alba_info.append(data)
    return alba_info


def make_file(alba_info, company):
    file = open(f"{company}.csv", mode="w", encoding="utf-8-sig")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for alba in alba_info:
        writer.writerow(alba)


# 브랜드들의 리스트
super_brand_links, super_brand_companies = super_link(soup)

for n in range(len(super_brand_companies)):
    page_info = get_page_info(super_brand_links[n])
    alba_info = get_alba_info(page_info)
    make_file(alba_info, super_brand_companies[n])

