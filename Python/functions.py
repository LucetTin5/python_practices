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
    print("Hello! Please choose select a country by number:")
    for i in range(len(dic)):
        if type(dic[i]) is tuple:
            print(f"# {i}: {dic[i][0]}")
        else:
            print(f"# {i}: {dic[i]}")


def take_number(dic):
    try:
        number = int(input("# "))
        if number < 0 or number >= len(dic):
            print("Choose a number from the list.")
            take_number(dic)
        else:
            if type(dic[number]) == tuple:
                print(
                    f"You chose {dic[number][0]}\nThe currency code is {dic[number][1]}")
            else:
                print(
                    f"You chose {dic[number]}\nThis country don't have universal currency")
    except:
        print("That wasn't a number.")
        take_number(dic)
