
###############################
from bs4 import BeautifulSoup #
import requests               #
import re                     #         
###############################
links = []
song = input('Enter the songs name:')
#Gets the website
website = requests.get('https://www.lyricsmode.com/search.php?search='+song).text
soup = BeautifulSoup(website,'lxml')
#Finds for the links of the song
for a in soup.find_all('a', href=True):
    links.append(a['href'])
#Gets the weblink of the song lyric
song_website = requests.get('https://www.lyricsmode.com'+links[12]).text
song_soup = BeautifulSoup(song_website,'lxml')
#Prints the lyrics
try:
    lyrics = song_soup.find('div', id = "lyrics_text").text
    artist_name = song_soup.find('span', attrs={'class':'fs32'}).text
    print(f"Song Name|{song}\nLyrics:\n{lyrics}")        
#Scenario if any error is raised
except:
    print('Song not found in the database')

#Searching for youtube Link

yt_search = requests.get('https://www.youtube.com/results?search_query='+song+artist_name,'youtube+link').text
yt_soup = BeautifulSoup(yt_search, 'html.parser')
a = yt_soup.find_all("a", href=True)
for i in a:
    url = i.get('href')
    print(f'\t\t{url}')
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

