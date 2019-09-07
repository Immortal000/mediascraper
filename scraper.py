
###############################
from bs4 import BeautifulSoup #
import requests               #
import re                     #
###############################
links = []

'''
Format:
Song name:
Song artist:
Release date:
Song description, background information:
Music video link:
Lyrics(optional):
'''
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
    yt_links = []
    lyrics = song_soup.find('div', id = "lyrics_text").text
    #DONOT EDIT --- print(f'Song name:{Song}\nSong artist: {}')
    artist_name = song_soup.find('span', attrs={'class':'fs32'}).text
    google_search = requests.get('https://www.youtube.com/results?search_query='+song,artist_name).text
    google_soup = BeautifulSoup(google_search, 'lxml')
    for l in google_soup.find_all('a', href=True):
        yt_links.append(l['href'])
    print(f"Song Name| {song}\nYoutube Link|{yt_links[146]}\nLyrics:\n{lyrics}")
        
#Scenario if any error is raised
except:
    print('Song not found in the database')
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

