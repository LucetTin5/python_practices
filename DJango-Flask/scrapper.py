import requests
from bs4 import BeautifulSoup

def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find('div', {'class': 's-pagination'})
    links = pagination.find_all('a')
    page_num = []
    for link in links:
        page_num.append(link.get_text())
    last_page = page_num[-2]

    return int(last_page)


def extract_job_info(html, url):
    job_title = html.find('h2').find('a')['title']
    company_and_location = html.find('h3').find_all('span', recursive=False)
    company = company_and_location[0]
    if company:
        company = company.get_text(strip=True)
    else:
        company = None
    location = company_and_location[1].get_text(strip=True)
    job_id = html['data-jobid']
    apply_link = f"https://stackoverflow.com/jobs/{job_id}"
    return {
        'title': job_title,
        'company': company,
        'location': location,
        'link': apply_link
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO pages: page {page + 1}")
        # 0 ~ last-page - 1  page
        result = requests.get(f'{url}&pg={page + 1}')
        # 각 페이지의 결과값을 불러온 후 bs로 수정
        soup = BeautifulSoup(result.text, 'html.parser')
        # 직업이름, 기업이름, 직장의 위치, 지원 링크를 각각 불러온다.
        searched = soup.find_all('div', {'class': '-job'})
        for result in searched:
            info = extract_job_info(result, url)
            jobs.append(info)
    return jobs


def get_jobs(word):
    URL = f"https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL)
    return jobs
