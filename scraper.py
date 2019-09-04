from bs4 import BeautifulSoup 
import requests 
from bs4 import lxml
#All the websites used: 
websites = ['https://www.genius.com', 'https://www.shazam.com', 'https://www.musicbrainz.org']
song = input('Enter the songs name:')

#Extracting the music vieo 
website = requests.get('https://google.com/search?q=%s'+song+'song')
soup = BeautifulSoup(website, 'lxml')
