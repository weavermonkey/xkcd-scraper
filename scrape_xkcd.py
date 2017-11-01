from bs4 import BeautifulSoup
import time
import requests

initial_url = 'https://xkcd.com/'
current_url = ''

page_request = requests.get(initial_url)

while(page_request.status_code != 404):
	if current_url == '':
		current_page = requests.get(initial_url)
	else:
		current_page = requests.get(current_url)
	html_content = current_page.text
	soup_obj = BeautifulSoup(html_content,'lxml')
	comic_class_div = soup_obj.find('div',{'id':'comic'})
	curr_comic_title = comic_class_div.img['title']
	comic_nav_div = soup_obj.find('ul',{'class':'comicNav'})
	next_comic_url = comic_nav_div.find_all('a')[1]['href'].replace('/','')
	print curr_comic_title, next_comic_url
	current_url = initial_url + next_comic_url
	time.sleep(0.8)
	print '###################################################'
