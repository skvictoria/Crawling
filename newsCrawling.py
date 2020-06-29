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
