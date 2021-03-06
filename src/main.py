####################################################################
from bs4 import BeautifulSoup                                      #
import requests                                                    #
import re                                                          #         
####################################################################
#lyrics from https://www.lyricsmode.com
global song, artist_name, index
index = 12 
song = input('Song:')
def get_youtube_link(song,artist_name):
     yt_links = []
     website = requests.get('https://www.youtube.com/results?search_query='+song+artist_name+'video+song').text
     soup = BeautifulSoup(website, 'lxml')
     for link in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
          yt_links.append('https://www.youtube.com'+link['href'])
     print(f'Youtube link for the song:{yt_links[0]}')

     
def get_lyrics(song, index):
     links = []
     website = requests.get('https://www.lyricsmode.com/search.php?search='+song).text
     soup = BeautifulSoup(website,'lxml')
     for a in soup.find_all('a', href=True):
         links.append(a['href'])
     song_website = requests.get('https://www.lyricsmode.com'+links[index]).text
     song_soup = BeautifulSoup(song_website,'lxml')
     try: 
          lyrics = song_soup.find('div', id = "lyrics_text").text.strip()
          artist_name = song_soup.find('span', attrs={'class':'fs32'}).text
          print(f"Song Name|{song}\nArtist Name|{artist_name}\n")
     except: 
         print('Song not found in database')
     answer = input('Is this the right song?')
     if answer == 'yes':
          print(f"Lyrics:\n{lyrics}")     
          get_youtube_link(song,artist_name)
     else:
          index = index + 2 
          get_lyrics(song,index)
get_lyrics(song,index)
