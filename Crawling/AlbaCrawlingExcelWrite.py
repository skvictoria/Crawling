import xlsxwriter as xw

wb = xw.Workbook(r"알바공고.xlsx")
ws = wb.add_worksheet("sheet 1")

urls = 'http://www.alba.co.kr/Main.asp?utm_source=google&utm_medium=paidsearch&utm_campaign=brand&utm_content=pc_cpc&utm_term=%EC%95%8C%EB%B0%94%EC%B2%9C%EA%B5%AD&gclid=CjwKCAjw_-D3BRBIEiwAjVMy7Ke-sioXDn7jORjKCI7MLryfJ612AVS8UZWj3iaWltX7uxSrNZ6lzxoCnSUQAvD_BwE'
res = requests.get(urls)
news_bs = bs4.BeautifulSoup(res.text)


wholebox=news_bs.find('ul',class_='goodsBox')


tmp = wholebox.find_all('a', class_= 'goodsBox-info')
ws.write(0,0,'알바명')
ws.write(0,1,'알바지역')

l = 1    
for i in tmp:
    ws.write(l,0,i.find('span', class_='title').text)
    ws.write(l,1,i.find('span', class_ = 'local').text)
    l = l+1

wb.close()   ## ws.close가 아니다.
