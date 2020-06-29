import xlsxwriter as xw

title_list=[]
href_list = []
content_list = []
url='https://search.daum.net/search?w=news&sort=recency&q={}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p={}&rc=1&at=more&sd=&ed=&period='
    
for p in range(1, page+1):
    real_url = url.format(search,page)

    res = requests.get(real_url)
    news_bs = bs4.BeautifulSoup(res.text)

    div_list = news_bs.find_all('div', class_='cont_inner')
    title_list = list(map(lambda x: x.find('a').text, div_list))
    href_list = list(map(lambda x: x.find('a')['href'], div_list))
    content_list = list(map(lambda x: x.find('p').text, div_list))

wb = xw.Workbook(r"현재 뉴스.xlsx")
ws = wb.add_worksheet("sheet 1")

ws.write_row(0,0,['번호','제목','링크','내용'])
'''
ws.write(0,0,'제목')
ws.write(0,1,'링크')
ws.write(0,2,'내용')
'''
ws.write_column(1,0, list(range(1,len(title_list)+1)))
ws.write_column(1,1,title_list)
ws.write_column(1,2,href_list)
ws.write_column(1,3,content_list)


wb.close()   ## ws.close가 아니다.
