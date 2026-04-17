import time

import requests
from bs4 import BeautifulSoup
import csv, random


# htmlda = '''
# <p> dsb <p>
# <p>导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
#                             1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情</p>'''
#
# soup = BeautifulSoup(htmlda,"lxml")
# print([i.text for i in soup.find_all("p")])


htmlda = '''<div class="bd">
                        <p>
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>

                        
                        <div>
                            <span class="rating5-t"></span>
                            <span class="rating_num" property="v:average">9.7</span>
                            <span property="v:best" content="10.0"></span>
                            <span>3244298人评价</span>
                        </div>

                            <p class="quote">
                                <span>希望让人自由。</span>
                            </p>
                    </div>'''

soup = BeautifulSoup(htmlda,"lxml")

dadivlst = soup.find_all("div")                            #  dadiv = soup.find_all("div",class='')       这个是寻找div 且 class为空的
dadiv = dadivlst[len(dadivlst)-1]

pjspanlst = dadiv.find_all("span")
pjspan = pjspanlst[len(pjspanlst)-1]



print(pjspan.text)
# print(len(dadiv),dadiv[1])
# pjspan = dadiv.find_all("span")[len(dadiv.find_all("span"))-1]
#
# print(pjspan)








