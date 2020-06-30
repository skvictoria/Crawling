import requests
import bs4

class DaumNews:
    def __init__(self, title, page1=1, page2=1):
        self.__url__ = 'https://search.daum.net/search?w=news&sort=recency&q={}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p={}&rc=1&at=more&sd=&ed=&period='
        self.__url__ = self.__url__.format(title, page1)
        self.setPage(page1, page2)
        self.setTitle(title)
    
    def setPage(self, page1, page2):
        self.__page__ = page1
        if page2:
            self.__page2__ = page2
        else:
            self.__page2__ = page1
    
    def setTitle(self, title):
        self.__title__ = title
    
    def getNews(self, page1, page2):
        title_list = []
        href_list=[]
        content_list=[]
        
        for i in range(page1, page2+1):
            
            res = requests.get(self.__url__)
            news_bs = bs4.BeautifulSoup(res.text)

            div_list = news_bs.find_all('div', class_='cont_inner')
            title_list += list(map(lambda x: x.find('a').text, div_list))
            href_list += list(map(lambda x: x.find('a')['href'], div_list))
            content_list += list(map(lambda x: x.find('p').text, div_list))
        
        return title_list, href_list, content_list

news = DaumNews("날씨")
news.getNews(1,2)


'''
def print_news(search,page):
    title_list=[]
    href_list = []
    content_list = []
    url='https://search.daum.net/search?w=news&sort=recency&q={}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p={}&rc=1&at=more&sd=&ed=&period='
    
    for p in range(1, page+1):
        real_url = url.format(search,page)

        res = requests.get(real_url)
        news_bs = bs4.BeautifulSoup(res.text)

        div_list = news_bs.find_all('div', class_='cont_inner')
        for div in div_list:
            title_list.append(div.find('a').text)
            href_list.append(div.find('a')['href'])
            content_list.append(div.find('p').text)
        
    return title_list, href_list, content_list
        
print_news('현대차',2)
'''
