import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=javascript&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')
    page_num = []
    for link in links:
        page_num.append(link['aria-label'])
    last_page = page_num[-2]
    
    return int(last_page)


def extract_job_info(html):
    job_title = html.find('h2',{'class': 'title'}).find('a')['title']
    company_and_location = html.find('div', {'class': 'sjcl'})
    company = company_and_location.find('span', {'class': 'company'})
    if company:
        company = company_and_location.find('span', {'class': 'company'}).get_text(strip=True)
    else:
        company = None
    location = company_and_location.find('div', {'class': 'recJobLoc'})['data-rc-loc']
    link_id = html['data-jk']
    apply_link = f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={link_id}"
    return {'title': job_title, 'company': company, 'location': location, 'apply_link': apply_link}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed pages: page {page}")
        # 0 ~ last-page - 1  page
        result = requests.get(f'{URL}&start={page * LIMIT}')
        # 각 페이지의 결과값을 불러온 후 bs로 수정
        soup = BeautifulSoup(result.text, 'html.parser')
        # 직업이름, 기업이름, 직장의 위치, 지원 링크를 각각 불러온다.
        searched = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
        for result in searched:
            info = extract_job_info(result)
            jobs.append(info)
    return jobs


def indeed_js_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs