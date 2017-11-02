from bs4 import BeautifulSoup
import time
import requests
import os
import urllib

initial_url = 'https://xkcd.com/'
current_url = ''

page_request = requests.get( initial_url )

while( page_request.status_code != 404 ):
	if current_url == '':
		current_page = requests.get( initial_url )
	else:
		current_page = requests.get( current_url )
	html_content = current_page.text
	soup_obj = BeautifulSoup( html_content,'lxml' )
	curr_comic_title = soup_obj.find( 'div', {'id':'comic'} ).img['title']
	curr_image_url = 'http:'+ soup_obj.find( 'div',{'id':'comic'} ).img['src']
	next_comic_url = soup_obj.find( 'ul',{'class':'comicNav'} ).find_all('a')[1]['href'].replace( '/', '' )
	current_url = initial_url + next_comic_url
	comic_path_on_local = str( int( next_comic_url ) + 1 )
	os.mkdir( comic_path_on_local )
	alt_text_file = open( ( os.path.join( os.getcwd(), comic_path_on_local ) ) + '/' + comic_path_on_local + '.txt', 'w' )
	alt_text_file.write( curr_comic_title )
	alt_text_file.close()
	urllib.urlretrieve( curr_image_url, os.path.join( os.getcwd(), comic_path_on_local ) + '/' + comic_path_on_local +'.png' )
	time.sleep( 0.8 )
