def get_info_from_tag(tag):
    tag = str(tag)
    a = tag.find('>')
    tag = tag[a + 1:]
    a = tag.find('<')
    tag = tag[:a]
    return tag

# Копирование песни с аккордами с amdm.ru
def get_song_from_number(song):
    import requests
    url = 'https://amdm.ru/akkordi/ /' + song + '/ /'
    request = requests.get(url)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find('pre', itemprop='chordsBlock')
    return main_content.text

# Копирование песни с аккордами с amdm.ru с разметкой строк
def get_splited_song_from_number(song):
    import requests
    url = 'https://amdm.ru/akkordi/ /' + song + '/ /'
    request = requests.get(url)

    # Получение блока песни с html разметкой
    start_block = request.text.find('<pre itemprop="chordsBlock">') + 28
    end_block = request.text[start_block:].find('</pre>')
    block = request.text[start_block:start_block + end_block]
    block = block.split('\n')
    block_markup = list()

    for el in block:
        if el.find('<b>') != -1:
            block_markup.append('chords')
        else:
            block_markup.append('text')

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find('pre', itemprop='chordsBlock')
    main_content = main_content.text.split('\n')

    # splited_block = list()
    # for el in range(len(block_markup)):
    #     if block_markup[el] == 'chords':
    #         splited_block.append(main_content[el])
    #     else:
    #         splited_block[len(splited_block) - 1] += '\n' + main_content[el]

    return main_content, block_markup

# Узнавание номера песни
def get_song_number(song):
    import requests
    url = 'https://amdm.ru/search/?q=' + song
    request = requests.get(url)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find('td', class_='artist_name').find_all('a')[1].get('href')
    return main_content.replace('/', '', 4)[main_content.replace('/', '', 4).find('/') + 1:main_content.replace('/', '', 5).find('/') + 1]

def get_song_info_1(song):
    import requests
    url = 'https://amdm.ru/search/?q=' + song
    request = requests.get(url)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find_all('a', class_='artist')
    return get_info_from_tag(main_content[0])

def get_song_info_2(song):
    import requests
    url = 'https://amdm.ru/search/?q=' + song
    request = requests.get(url)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.text)

    main_content = soup.find_all('a', class_='artist')
    return get_info_from_tag(main_content[1])

def get_song(song):
    return get_song_from_number(get_song_number(song))

def get_splited_song(song):
    return get_splited_song_from_number(get_song_number(song))