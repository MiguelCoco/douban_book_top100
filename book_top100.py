
import urllib.request as urequest
from bs4 import BeautifulSoup as bs

#{}每下一页面start值增加25
top100_url = 'https://book.douban.com/top250?start={}'

with open('book_top100_info.txt','a') as outputfile:
	#共10页面，每一页面25条信息
	for i in range(4):
		start = i*25
		all_url = top100_url.format(start)
		#打开、读取URL内容
		url_content = urequest.urlopen(all_url).read()
		#解析html
		soup = bs(url_content,'html.parser')
		#提取100条主要信息
		all_items = soup.find_all(class_='item')
		for item in all_items:
			item_href = item.find(class_='pl2').find('a')['href']
			book_title = item.find(class_='pl2').find('a')['title']
			book_desc = item.find(class_="inq").get_text() 	
			outputfile.write('{} {} {}\n'.format(item_href,book_title,book_desc))
			print('{} {}  {}'.format(item_href,book_title,book_desc))	
