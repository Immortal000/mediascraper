
###############################
from bs4 import BeautifulSoup #
import requests               #
import re                     #         
###############################
global song, artist_name, index
index = 12 
song = input('Song:')
def get_lyrics(song, index):
     links = []
     website = requests.get('https://www.lyricsmode.com/search.php?search='+song).text
     soup = BeautifulSoup(website,'lxml')
     for a in soup.find_all('a', href=True):
         links.append(a['href'])
     song_website = requests.get('https://www.lyricsmode.com'+links[index]).text
     song_soup = BeautifulSoup(song_website,'lxml')
     
     lyrics = song_soup.find('div', id = "lyrics_text").text
     artist_name = song_soup.find('span', attrs={'class':'fs32'}).text
     print(f"Song Name|{song}\nArtist Name|{artist_name}\nLyrics:\n{lyrics}")     
     '''except: 
         print('Song not found in database')'''
     answer = input('Is this the right song?')
     if answer == 'no':
          index = index + 2
          get_lyrics(song,index)
     else:
          continue
get_lyrics(song,index)

#Searching for youtube Link
'''yt_links = []
yt_search = requests.get('https://www.bing.com/videos/search?q='+song+artist_name,'youtube+link').text
yt_soup = BeautifulSoup(yt_search, 'html.parser')
a = yt_soup.findAll("div",{"class":"mc_vtvc"})
for i in a:
    print(i)
for i in a:
    yt_links.append(i.get('href'))
print(yt_links)''' 

#file digestion

def file_digest():
    fileQ = 5 #placeholder value
    #fileQ is the number of files
    while fileQ != 0:
        '''
        Placeholder for the file input function using f.
        '''
        fileQ -= 1
file_digest()

#Working on the formatting 

