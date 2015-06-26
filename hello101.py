from urllib.parse import urlparse
from bs4 import BeautifulSoup,SoupStrainer
import requests
import time

#BASE_URL = "http://genius.com"
#artist_url = "http://genius.com/artists/Pink-floyd"
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#browser = webdriver.Firefox()
#browser.get(artist_url)
#elem=browser.find_element_by_tag_name("body")

#pagedown=300
#while pagedown:
 #   elem.send_keys(Keys.DOWN)
  #  time.sleep(0.1)
   # pagedown=pagedown-1
    #print (pagedown)

#post_elems=browser.find_element_by_class_name("song_title")

#I used Selenium to scroll till bottom (had infinite scroll)
# and saved the result in a html file Commented part in the code is of scraping.

#BASE_URL = "http://genius.com"

#artist_url = "http://genius.com/artists/Pink-floyd"


html=open('pfsongslist.html').read()

songsList = SoupStrainer('section',{'class': 'all_songs'})

souplyrics=SoupStrainer('div',{'class':'lyrics'})

songsLink=[]
songLyrics=[]
#songdetails={}
count=0
listOfSongs = BeautifulSoup(html,parse_only=songsList)
for a in listOfSongs.findAll('a',{'class':'song_link' }):
    songsLink.append(a['href'])
    #print (a['title'])

for i in songsLink:
    response=requests.get(i)
    lyrics=BeautifulSoup(response.text,parse_only=souplyrics)
    for p in lyrics.findAll('p'):
        songLyrics.append(p.text)
    count=count+1
    print("At Song %d . Remaining : %d "%(count,len(songsLink)-count))


print (songsLyrics)

