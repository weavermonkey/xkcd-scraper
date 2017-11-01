from bs4 import BeautifulSoup
import time
import requests
import os
import urllib


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
	curr_comic_title = soup_obj.find('div',{'id':'comic'}).img['title']
	curr_image_url = 'http:'+ soup_obj.find('div',{'id':'comic'}).img['src']
	next_comic_url = soup_obj.find('ul',{'class':'comicNav'}).find_all('a')[1]['href'].replace('/','')
	print curr_comic_title, next_comic_url,curr_image_url
	current_url = initial_url + next_comic_url
	os.mkdir(str(int(next_comic_url)+1))
	alt_text_file = open( ( os.path.join( os.getcwd(), str(int(next_comic_url)+1) ) ) + '/' + str(int(next_comic_url)+1) + '.txt', 'w' )
	alt_text_file.write(curr_comic_title)
	alt_text_file.close()
	urllib.urlretrieve( curr_image_url, os.path.join(os.getcwd(), str(int(next_comic_url)+1)) + '/' +str(int(next_comic_url)+1)+'.png' )
	time.sleep(0.8)