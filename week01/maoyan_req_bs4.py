# 引入requests和BeautifulSoup包
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd

# 猫眼电影页面
myurl = 'https://maoyan.com/films?showType=3'
ua = UserAgent(verify_ssl = False)
# 随机返回头部信息
user_agent = ua.random
header = {'user-agent':user_agent}
response = requests.get(myurl, headers = header)
print(response.status_code)
# 解析网页
bs_info = bs(response.text, 'html.parser')
hrefs = []
# 获取前10个电影链接
for tags in bs_info.find_all('div',class_='channel-detail movie-item-title'):
    for a_tag in tags.find_all('a'):
        href = a_tag.get('href')
        hrefs.append(href)


# print(hrefs[:10])
url_list = hrefs[:10]

# 获取前10个电影的名称、类型和上映时间
for url in url_list:
    de_url = f'https://maoyan.com{url}'
    ua_2 = UserAgent(verify_ssl = False)
    # 随机返回头部信息
    user_agent_2 = ua_2.random
    header_2 = {'user-agent':user_agent_2}
    response_2 = requests.get(de_url, headers = header_2)
    print(response.status_code)


# my_movie = pd.DateFrame(data = mylist)
# my_movie.to_csv('./my_movie.csv', encoding = 'utf8', index = False, header = False)
            