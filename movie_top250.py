
import urllib.request as urequest
from bs4 import BeautifulSoup as bs

#{}每下一页面start值增加25
top250_url = 'https://movie.douban.com/top250?start={}&filter='

with open('movie_top250_info.txt','a') as outputfile:
	#共10页面，每一页面25条信息
	for i in range(10):
		start = i*25
		all_url = top250_url.format(start)
		#打开、读取URL内容
		url_content = urequest.urlopen(all_url).read()
		#解析html
		soup = bs(url_content,'html.parser')
		#提取250条主要信息
		all_items = soup.find_all(class_='item')
		for item in all_items:
			ranking = item.find('em').get_text()
			item_href = item.find('a')['href']
			movie_title = item.find('img')['alt']
			#提取结果写入文件中
			outputfile.write('{} {} {}\n'.format(ranking,item_href,movie_title))
			print('{} {} {}'.format(ranking,item_href,movie_title))
