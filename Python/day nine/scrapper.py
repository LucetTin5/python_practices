import requests
import os

os.system("cls")

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"

# 리스트에서 타이틀~ 오브젝트 아이디를 뽑아 튜플로 리스트화 한다.
def make_info(li):
    info = []
    for item in li:
        title = item["title"]
        author = item["author"]
        url = item["url"]
        point = item["points"]
        comments = item["num_comments"]        
        user_id = item["objectID"]
        info.append((title, author, url, point, comments, user_id))
    return info

# 뉴, 포퓰러를 받아 make_info를 통해 데이터리스트를 만든다.
def get_story(url):
    req = requests.get(url)
    result = req.json()
    story_list = result["hits"]

    return make_info(story_list)

# 코멘트

def get_comments(objectID):
    url = make_detail_url(objectID)
    req = requests.get(url)
    result = req.json()
    story = result
    story_info = [story["title"], story["author"], story["url"], story["points"]]
    comment_list = story["children"]
    comments = []
    for comment in comment_list:
        if comment["author"]:
            comments.append([comment["author"], comment["text"].strip()])
        else:
            comments.append(["deleted"])
    return comments
get_comments(16582136)