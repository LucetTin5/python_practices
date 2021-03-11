import os
import requests as rq
from bs4 import BeautifulSoup

# 윈도우즈 cls, linux와 mac 는 clear
os.system("cls")
url = "https://www.iban.com/currency-codes"


def get_data(url):
    # url에서 html을 추출
    r = rq.get(url)
    # html을 parser로 정리
    soup = BeautifulSoup(r.text, "html.parser")
    # soup에서 table 내의 값을 추출
    table = soup.find("table", {"class": "table"})
    # table에서 각 값들을 추출
    data = list(table.find_all('td'))

    # data 내의 모든 값을 string으로 전환
    for i in range(len(data)):
        data[i] = data[i].string
    for n in range(len(data)):
        if data[n] == None:
            data[n] = "no data"

    return data


# data에서 나라와 통화를 추출
def get_items(data):
    con = []
    cur = []
    for i in range(len(data)//4):
        con.append(data[4 * i])
        cur.append(data[4 * i + 2])
    merged_data = []
    for n in range(len(con)):
        merged_data.append((con[n], cur[n]))
    return merged_data


def main(li):
    print("Hello! Please choose select a country by number:")
    for i in range(len(li)):
        print(f"# {i} {li[i][0]}")

def get_ans(li):
    try:
        ui = user_input = int(input("#: "))
        if type(ui) != int:
            raise Exception
        elif ui < 0 or ui > len(li):
            print("Choose a number from the list.")
            get_ans(li)
    except:
        print("That wasn't a number.")
        get_ans(li)
    finally:
        ui = int(ui)
        if li[ui][1] != "no data":
            print(f"You chose {li[ui][0]}\nThe currency code is {li[ui][1]}")
        else:
            print(f"You chose {li[ui][0]}\nThis country don't have universal currency")
        quit()


data = get_data(url)
# 나라와 통화를 리스트에 저장
country_currency = get_items(data)
main(country_currency)
get_ans(country_currency)