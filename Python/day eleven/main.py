import requests
from os import system
from bs4 import BeautifulSoup as bs
from flask import Flask, render_template, request

system("cls")

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""
db = {}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


# div class scrollerItem > div1 > div > btn upvote div : upvote
# scrollerItem > div data-click-id background > a > h3  : title / a
def make_soup(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    requests = requests.get(url, headers=headers)
    soup = bs(get_requests.text, "html.parser")
    
    return soup


def extract_data(soup):
    scrollerItem = soup.find_all("div", {"class": "scrollerItem"})
    item_list = []
    for i in range(len(scrollerItem)):
        if i == 1:
            pass
        else:
            item_id = scrollerItem[i]["id"]
            item_link = scrollerItem[i].find("a", {"data-click-id": "body"})["href"]
            item_title = scrollerItem[i].find("h3").string
            item_upvote = scrollerItem[i].find("div", {"id": f"vote-arrows-{item_id}"}).get_text()
            item_info = (item_id, item_link, item_title, item_upvote)
            item_list.append(item_info)
    return item_list




"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""





app = Flask("DayEleven")

@app.route("/")
def home():

    return render_template("home.html", subreddits=subreddits)

app.run(host="127.0.0.1")