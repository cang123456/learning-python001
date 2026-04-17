import re

import requests

from bs4 import BeautifulSoup
import db_connet


def solve(i):
    url = f'https://movie.douban.com/top250?start={i*25}&filter='
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
    }

    res = requests.get(url=url,headers=header)

    soup = BeautifulSoup(res.text,'lxml')

    li_list = soup.select(".grid_view li")


    for li in li_list:
        name = '' + li.select(".info .hd span")[0].string
        image_url = '' + li.select("img")[0].get("src")
        rankings = '' + li.select("em")[0].string
        movie_rating = '' + li.select(".rating_num")[0].string
        movie_author = '' + li.select(".bd p")[0].get_text()
        movie_author = re.sub('[\xa0;\n\t ]','',movie_author)
        numofeva = '' + li.select(".bd div span")[-1].string
        movie_lab = li.select(".quote span")[0].string if li.select(".quote span") else ''
        print(rankings,name,image_url,movie_rating,movie_author,numofeva,movie_lab)

        answer =  (rankings, name, image_url, movie_rating, movie_author, numofeva, movie_lab)
        
        db_connet.solve(answer)




for i in range(25):
    solve(i)



























