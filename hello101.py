from urllib.parse import urljoin
from bs4 import BeautifulSoup,SoupStrainer
import requests
import time

BASE_URL = "http://www.azlyrics.com"
artist_url = "http://www.azlyrics.com/p/pinkfloyd.html"
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#browser = webdriver.Firefox()
#browser.get(artist_url)
#elem=browser.find_element_by_tag_name("body")
#htmlfile=browser.page_source
#soupAllSongs=BeautifulSoup(htmlfile,"lxml")
#print(soupAllLinksParse)
#pagedown=300
#while pagedown:
 #   elem.send_keys(Keys.DOWN)
  #  time.sleep(0.1)
   # pagedown=pagedown-1
    #print (pagedown)
#post_elems=browser.find_element_by_class_name("song_title")
#I used Selenium to scroll till bottom (had infinite scroll)
# and saved the result in a html file Commented part in the code is of scraping.
'''
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
    time.sleep(5)
'''

'''Above method was using Genius.com for scraping but the requests were taking a lot of time
and I got connection timeout after several requests, so it wasn't practically possible to use
it. So I shifted over to a lightweight more cleaner lyrics source, azlyrics.com
Also, I tried using Musixmatch API but felt that scraping is more suitable for this project.
Though that service is nice and I will consider it in my future projects'''

htmlfile=open('pfaz.html').read()
soupAllLinks=SoupStrainer('a',{'target': '_blank'})

soupAllLinksParse=BeautifulSoup(htmlfile,parse_only=soupAllLinks)

songLinks=[]
songLyrics=[]
count=0

for i in soupAllLinksParse.findAll('a'):

    if i['href'][:2] !='..':
        pass
    else:
        #print(i['href'])
        link=urljoin(BASE_URL,i['href'][2:])
        songLinks.append(link)

#print(songLinks[142:])

data = open("lyricsLast.txt", "a")


for i in songLinks[143:]:
    print(i)
    try:
        response=requests.get(i, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        print ("Status Code : %d "%(response.status_code))
        lyrics=BeautifulSoup(response.text)
        cleaned=lyrics.findAll('div')[22].text.replace("\n"," ").replace("\r"," ").strip()
        data.write(cleaned)
        count=count+1
        print("At Song %d . Remaining : %d "%(count,len(songLinks)-count))
        time.sleep(15)
    except requests.exceptions.ConnectionError:
        print("Bad Req")


data.close()
print(songLyrics)
print (len(songLyrics))

