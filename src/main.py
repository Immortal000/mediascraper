
###############################
from bs4 import BeautifulSoup #
import requests               #
import re                     #         
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH # 
###############################
global song, artist_name, index
index = 12 
song = input('Song:')
def get_youtube_link(song,artist_name):
     yt_links = []
     website = requests.get('https://www.youtube.com/results?search_query='+song+artist_name+'video+song').text
     soup = BeautifulSoup(website, 'lxml')
     for link in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
          yt_links.append('https://www.youtube.com'+link['href'])
     print(yt_links[0])

     
def get_lyrics(song, index):
     links = []
     website = requests.get('https://www.lyricsmode.com/search.php?search='+song).text
     soup = BeautifulSoup(website,'lxml')
     for a in soup.find_all('a', href=True):
         links.append(a['href'])
     song_website = requests.get('https://www.lyricsmode.com'+links[index]).text
     song_soup = BeautifulSoup(song_website,'lxml')
     try: 
          lyrics = song_soup.find('div', id = "lyrics_text").text
          artist_name = song_soup.find('span', attrs={'class':'fs32'}).text
          print(f"Song Name|{song}\nArtist Name|{artist_name}\nLyrics:\n{lyrics}")     
     except: 
         print('Song not found in database')
     answer = input('Is this the right song?')
     if answer == 'no':
          index = index + 2
          get_lyrics(song,index)
     else:
          get_youtube_link(song,artist_name)
get_lyrics(song,index)


#file digestion

def file_digest():
    fileQ = 5 #placeholder value
    #fileQ is the number of files
    while fileQ != 0:
         # Create MP3File instance.
        mp3 = MP3File("test.mp3")
        alb = mp3.album

        #get the music tags
        mp3Tags = mp3.get_tags()
        
        fileQ -= 1
file_digest()

#Working on the formatting 

