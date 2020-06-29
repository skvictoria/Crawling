urls = 'http://www.alba.co.kr/Main.asp?utm_source=google&utm_medium=paidsearch&utm_campaign=brand&utm_content=pc_cpc&utm_term=%EC%95%8C%EB%B0%94%EC%B2%9C%EA%B5%AD&gclid=CjwKCAjw_-D3BRBIEiwAjVMy7Ke-sioXDn7jORjKCI7MLryfJ612AVS8UZWj3iaWltX7uxSrNZ6lzxoCnSUQAvD_BwE'
res = requests.get(urls)
news_bs = bs4.BeautifulSoup(res.text)


wholebox=news_bs.find('ul',class_='goodsBox')


tmp = wholebox.find_all('a', class_= 'goodsBox-info')

for i in tmp:
    print(i.find('span', class_='title').text)
    print(i.find('span', class_ = 'local').text)
    print('*'*60)
'''
tmps = tmp.find('span', class_='title').text

lists = []
for i in tmp.find_all('span', class_='title'):
    lists.append(i.text)

print(tmps)
'''
