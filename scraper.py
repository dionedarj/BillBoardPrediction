from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.request
import json
import getpass


def list_from_date(date):  
    #First Song/Artist - needed because Billboard puts their first song/artist in a div class "chart-number-one__title"  and "chart"
 
    first_song = soup.find('div', {'class': 'chart-number-one__title'}).string.strip()
    first_artist = soup.find('div', {'class': 'chart-number-one__artist'}).find('a', text=True).string.strip()

    songs = soup.find_all('span', {'class': 'chart-list-item__title-text'})
    artists = soup.find_all(lambda tag: (tag.name == 'div' and tag.get('class') == ['chart-list-item__artist'] and len(list(tag.descendants)) == 1) 
                                    or (tag.name == 'a' and tag.parent.name == 'div' and tag.parent.get('class') == ['chart-list-item__artist']))

    songs = list(map(lambda x: x.contents[0].strip(), songs))
    artists = list(map(lambda x: x.contents[0].strip(), artists))

    songs = [first_song] + songs
    artists = [first_artist] + artists

    print('Number of songs on list: ' + str(len(songs)))
    print('Number of artists on list: ' + str(len(artists)))

    pairs = list(zip(artists,songs))
 
    print (pairs)
    return pairs

if __name__ == '__main__':
    # client = dc.Client('BillBoardStats/0.1')
    token = getpass.getpass(prompt='What is your user token?')
    # client = dc.Client('BillBoardStats/0.1', user_token='')
    results = client.search('Psycho', type='release')
    print (results[0].artists[0].name)