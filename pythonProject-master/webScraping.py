import requests

from bs4 import BeautifulSoup

# pagina que vamos trabalhar
url = 'https://www.kabum.com.br/hardware/placa-de-video-vga'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='sc-ff8a9791-7 JDtDP productCard')
#não pegou última página
ultima_pagina = soup.find('a', class_='page').get_text().strip()

for i in range(1,int(10)):
    url_pag = f'https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    placas = soup.find_all('div', class_='sc-ff8a9791-7 JDtDP productCard')

    with open('preco_placas_video.csv','a',newline='',encoding='UTF-8') as csv:
        for placa in placas:
            marca = placa.find('span', class_='sc-d99ca57-0 bzucsr sc-ff8a9791-16 kMfyNu nameCard').get_text().strip()
            preco = placa.find('span', class_='sc-3b515ca1-2 hQOqhY priceCard').get_text().strip()

            try:
                preco = placa.find('span', class_='sc-3b515ca1-2 hQOqhY priceCard').get_text().strip()
                num_preco = preco[2:]
                #num_preco = num_preco[:-3]
            except:
                num_preco = '0'

            linha = marca + ';' + preco + ';' + num_preco
            print(linha)
            csv.write(linha)
    print(url_pag)

