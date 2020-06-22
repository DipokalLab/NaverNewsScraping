import requests as req
from bs4 import BeautifulSoup
from flask import Flask

app = Flask (__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search/<numbers>/<keyword>') 
def hello_user(numbers, keyword):
    search_keyword = keyword
    temp = []

    k = 0
    for i in range(int(numbers)):
        if i == 1:
            k = i*11
        else:
            k = i*10

        url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}&sort=1&sm=tab_pge&start={k}'

        r = req.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        titles = soup.select('.news .type01 li dt a[title]')

        for title in titles:
            print(title['title'])
            temp.append(title['title'])

    return str(temp)
 
if __name__ == "__main__":
    app.run()
    
    
