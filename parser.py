import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def get_page_data(session, url_):
    """Функция собирает данные со страницы"""
    headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,image/webp, */*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/112.0.0.0 Safari/537.36'
    }
    async with session.get(url=url_, headers=headers) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, 'html.parser')
        model = soup.find_all('h3', 'listing-item__title')
        key = url_.split('/')

        links_per_model[f'{key[-2]} {key[-1]}'.upper()] = []
        for link in model:
            l = link.a.attrs.get('href')
            links_per_model[f'{key[-2]} {key[-1]}'.upper()].append('https://cars.av.by' + l)


async def gather_data():
    """Функция формирует список ссылок на модели Audi и список задач"""

    async with ClientSession() as session:
        headers = {
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,image/webp, */*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/112.0.0.0 Safari/537.36'
        }
        async with session.get(url='https://cars.av.by/audi', headers=headers) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, 'html.parser')
            models = soup.find_all('li', 'catalog__item')

            for link in models:
                if link.text.startswith('80'):
                    model_80_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('90'):
                    model_90_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('100'):
                    model_100_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('200'):
                    model_200_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif 'A' in link.text:
                    model_A_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('Q'):
                    model_Q_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('R'):
                    model_R8_RS_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('S'):
                    model_S_SQ_links.append('https://cars.av.by' + link.a.attrs.get('href'))
                elif link.text.startswith('TT'):
                    model_TT_TTS_links.append('https://cars.av.by' + link.a.attrs.get('href'))
            tasks = []
            for model in models_links:
                for url in model:
                    task = asyncio.create_task(get_page_data(session, url))
                    tasks.append(task)
            await asyncio.gather(*tasks)


def parser_run():
    asyncio.run(gather_data())


model_80_links = []
model_90_links = []
model_100_links = []
model_200_links = []
model_A_links = []
model_Q_links = []
model_R8_RS_links = []
model_S_SQ_links = []
model_TT_TTS_links = []
models_links = (
    model_80_links, model_90_links, model_100_links,
    model_200_links, model_A_links, model_Q_links,
    model_R8_RS_links, model_S_SQ_links, model_TT_TTS_links
)

links_per_model = {}

parser_run()
