import requests as re
from bs4 import BeautifulSoup
def getData(url):
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
        "content-type":"application/json"
    }
    web=re.get(url,headers=headers)
    web.encoding="utf-8"
    return web.text


url1="https://www.apple.com/tw/shop/refurbished/mac"
data=getData(url1)
soup = BeautifulSoup(data, "html.parser")

titles=soup.find("div",class_="rf-refurb-category-grid-no-js")
titles=titles.find_all("li")


for index, title in enumerate(titles, start=1):
    
    print(f"Item {index}: {title.h3.a.string}")
    print("https://www.apple.com"+title.h3.a["href"])
    print(title.div.string)
   
