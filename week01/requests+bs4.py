import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
cookie = '__mta=150239753.1595246592119.1595332925935.1595542485990.7; uuid_n_v=v1; uuid=F9B75DF0CA8011EAB2AE8B45D9A9C865119372F35227413E9C64975C445D4CF0; mojo-uuid=7f4c703124a36d6b48e207b39862b4ec; _lxsdk_cuid=1736c1b3e26c8-088cabfab03c83-15366650-13c680-1736c1b3e26c8; _lxsdk=F9B75DF0CA8011EAB2AE8B45D9A9C865119372F35227413E9C64975C445D4CF0; _csrf=7fb3a68dbd261a37456193279d604aadf1e88a5f6d8e10b2f56657a02c4ee199; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595246591,1595331874,1595542409; mojo-session-id={"id":"165cdbca867f1595cc0762cae853d5a8","time":1595542412841}; __mta=150239753.1595246592119.1595542485990.1595542490271.8; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595543125; _lxsdk_s=1737dbd159a-75e-b2e-d81%7C%7C9'
header = {'user-agent' : user_agent, 'Cookie' :cookie}
myurl = "https://maoyan.com/films?showType=3"
response = requests.get(myurl,headers = header)
# print(response.text)
bs_info = bs(response.text , "html.parser")

# for tags in bs_info.find_all("div", attrs = {"class": "movie-hover-info"}):
#     print(tags.text)
#    for name in tags.find_all('span',attrs = {'class':'name'}):
#        for movie_type in tags.find_all('div', attrs = {'class':'movie-hover-title'}):
#            for show_time in tags.find_all('div',attrs={'class':'movie-hover-title movie-hover-brief'}):
                # print(name.text,movie_type.text,show_time.text)
            #    my_movielist = [name.text,movie_type.lsit,show_time.text]
            #    movielist = pd.DataFrame(data = my_movielist)
            #    movielist.to_csv('./movielist.csv',mode = 'a',encoding='utf-8')
            


    
# print(bs_info.find_all("div", attrs = {"class": "movie-hover-info"}))
# for tags in bs_info.find_all("div", attrs = {"class": "movie-hover-title"}):
#     print(tags.find('span').text)
for tags in bs_info.find_all('div',attrs = {'class': 'movie-hover-info'}):
    # print(tags.text)
    names = tags.find('span',attrs = {'class':'name'}).get_text()
    # print(names)
    movie_type = tags.find_all('div',attrs = {'class':'movie-hover-title'})[1].get_text().split()[-1]
    # print(movie_type)
    show_time = tags.find_all('div',attrs = {'class': 'movie-hover-title movie-hover-brief'})[0].get_text().split()[-1]
    # print(show_time)
    movie_list = [(names, movie_type, show_time)]
    title = [('moviename','movietype','showtime')]
    # print(movie_list)
    title = pd.DataFrame(data=title)
    movielist = pd.DataFrame(data = movie_list)
    title.to_csv('./movielist.csv',encoding='utf-8',index=False,mode='a',header= False)
    movielist.to_csv('./movielist.csv',encoding='utf-8',index=False,mode='a',header= False)


    