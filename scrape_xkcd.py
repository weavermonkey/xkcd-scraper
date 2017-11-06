import requests
from bs4 import BeautifulSoup
import os
import urllib
import time

initial_url = 'https://xkcd.com/'
next_url = ''

page_request = requests.get( initial_url )

while( page_request.status_code != 404 ):
	if next_url == '':
		current_page = requests.get( initial_url )
	else:
		current_page = requests.get( next_url )
	html_content = current_page.text
	soup_obj = BeautifulSoup( html_content,'lxml' )
	alt_text = soup_obj.find( 'div', {'id':'comic'} ).img['title'].encode('ascii','ignore').decode()
	comic_image_url = 'http:'+ soup_obj.find( 'div',{'id':'comic'} ).img['src']
	next_comic_number = soup_obj.find( 'ul',{'class':'comicNav'} ).find_all('a')[1]['href'].replace( '/', '' )
	comic_path_on_disk = str( int( next_comic_number ) + 1 )
	os.mkdir( comic_path_on_disk )
	alt_text_file = open( ( os.path.join( os.getcwd(), comic_path_on_disk ) ) + '/' + comic_path_on_disk + '.txt', 'w' )
	alt_text_file.write( alt_text )
	alt_text_file.close()
	urllib.urlretrieve( comic_image_url, os.path.join( os.getcwd(), comic_path_on_disk ) + '/' + comic_path_on_disk +'.png' )
	next_url = initial_url + next_comic_number
	time.sleep( 0.8 )
