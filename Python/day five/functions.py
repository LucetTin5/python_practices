import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

def get_data():
    os.system("clear")
    url = "https://www.iban.com/currency-codes"
    print("")
    result = requests.get(url)
    page_data = BeautifulSoup(result.text, "html.parser")
    table_data = page_data.find("table", {"class": "tablesorter"})
    data_list = list(table_data.find_all('td'))
    for i in range(len(data_list)):
        data_list[i] = data_list[i].string

    return data_list


def make_dic(list_x):
    country_currency = {}
    extracted_data = []
    for i in range(len(list_x)//4):
        if list_x[4 * i + 3] != None:
            appending_data = (list_x[4 * i], list_x[4 * i + 2])
        else:
            appending_data = (list_x[4 * i])
        extracted_data.append(appending_data)
    for n in range(len(extracted_data)):
        country_currency[n] = extracted_data[n]

    return country_currency


def call_data(dic):
    print("Welcome to currency convert.")
    for i in range(len(dic)):
        if type(dic[i]) is tuple:
            print(f"# {i}: {dic[i][0]}")
        else:
            print(f"# {i}: {dic[i]}")
    print("\nWhere are you from? Choose a country by number.")


def take_users(dic):
    try:
        user_country = int(input("#: "))
        if user_country >= len(dic):
            print("choose a number from the list.")
            take_users(dic)
        else:
            if type(dic[user_country]) == tuple:
                print(f"{dic[user_country][0]}")
                return dic[user_country][1]
            else:
                print(f"{dic[user_country]}")
                print("This country don't have universal currency, choose another country.")
                take_users(dic)
    except:
        print("That wasn't a number.")
        take_users(dic)

def take_another(dic):
    try:
        print("\nNow choose another country.")
        another_country = int(input("#: "))
        if another_country >= len(dic):
            print("choose a number from the list.")
            take_another(dic)
        else:
            if type(dic[another_country]) == tuple:
                print(f"{dic[another_country][0]}")
                return dic[another_country][1]
            else:
                print(f"{dic[another_country]}")
                print("This country don't have universal currency, choose another country.")
                take_another()
    except:
        print("That wasn't a number.")
        take_another(dic)


def take_change(cur1, cur2):
    url = f"https://transferwise.com/gb/currency-converter/{cur1}-to-{cur2}-rate?amount=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    exchange_rate = soup.find("h3", {"class":"cc__source-to-target"}).find("span", {"class": "text-success"}).string
    return float(exchange_rate)


def convert_currency(cur1, cur2):
    print("How many {0} do you want to convert to {1}?".format(cur1, cur2))
    exchange_rate = take_change(cur1, cur2)
    try:
        money = int(input())
        changed = money * exchange_rate
        start = format_currency(money, cur1, u'¤¤#,##0.00' , locale="en-US")
        end = format_currency(changed, cur2, u'¤ #,##0.00', locale="en-US")
        print(money, changed, start, end)
    except ValueError:
        print("That wasn't a number.")
        convert_currency(cur1, cur2)