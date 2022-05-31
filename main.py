# Копирование песни с аккордами с amdm.ru
def get_song_from_number(song):
    import requests
    url = 'https://amdm.ru/akkordi/ /' + song + '/ /'
    request = requests.get(url)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find('pre', itemprop='chordsBlock')
    return main_content.text

# Узнавание номера песни
def get_song_number(song):
    import requests
    url = 'https://amdm.ru/search/?q=' + song
    request = requests.get(url)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find('td', class_='artist_name').find_all('a')[1].get('href')
    return main_content.replace('/', '', 4)[main_content.replace('/', '', 4).find('/') + 1:main_content.replace('/', '', 5).find('/') + 1]

def get_song(song):
    return get_song_from_number(get_song_number(song))