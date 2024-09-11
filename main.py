import requests
import bs4


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all/'

response = requests.get(url)
soup=bs4.BeautifulSoup(response.text, features='lxml')

articles = soup.findAll('article', class_='tm-articles-list__item')

previews = dict()
for article in articles:
    date = article.time.text
    preview = article.find('h2', class_='tm-title tm-title_h2')
    title= article.find('a', class_='tm-title__link')
    href = title['href']
    previews.setdefault(date, [preview.text.strip(), url+href])
    print(f'<{date}>-<{preview.text.strip()}>-<{url +href}>')

for i in KEYWORDS:
    for j, k in previews.items():
        if i in k[0]:
            print(f'\n Результат поиска: "{i}": <{j}>-<{k[0]}>-><{k[1]}>')
            
