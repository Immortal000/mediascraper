from bs4 import BeautifulSoup 
import requests 
from bs4 import lxml

'''Format: 
Song name: 
Song artist: 
Release date: 
Song description, background information: 
Music video link: 
Lyrics(optional): ''' 

#All the websites used: 
websites = ['https://www.genius.com', 'https://www.shazam.com', 'https://www.musicbrainz.org']
song = input('Enter the songs name:')

#Extracting the music video
website = requests.get('https://google.com/search?q=%s'+song+'song')
soup = BeautifulSoup(website, 'lxml')
