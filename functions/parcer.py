import logging

import feedparser

from functions import send_logs_auto

logger2 = logging.getLogger(__name__)


async def get_news_headlines(n_news=2, url='https://news.rambler.ru/rss/politics/') -> list[dict[str]]:
    """
    Собирает новости и возвращает их в виде списка словарей.

    Пример вывода:

    ```
    output_list = [
        {"title": "Заголовок новости", "description": "Описание новости", "img_url": "https://i.pinimg.com/originals/34/52/a3/3452a32cab9e76f0c813afe1dc01f88e.jpg"},
        {"title": "Заголовок новости", "description": "Описание новости", "img_url": "https://i.pinimg.com/originals/34/52/a3/3452a32cab9e76f0c813afe1dc01f88e.jpg"},
    ]
    ```


    :param n_news: Количество новостей для получения.
    :type n_news: int
    :param url: Ссылка на rss-ленту
    :type url: str
    :return: Список словарей новостей `{"title": "Заголовок новости", "description": "Описание новости"}` или None в случае ошибки
    :rtype: list[dict[str]] | None
    """
    basic_output = [
        {"title": "Заголовок новости", "description": "Описание новости", "img_url": "https://i.pinimg.com/originals/34/52/a3/3452a32cab9e76f0c813afe1dc01f88e.jpg"},
        {"title": "Заголовок новости", "description": "Описание новости", "img_url": "https://i.pinimg.com/originals/34/52/a3/3452a32cab9e76f0c813afe1dc01f88e.jpg"},
    ]

    try:
        # Создаем объект feedparser для работы с RSS лентой
        feed = feedparser.parse(url)

        # Проверяем успешность загрузки RSS ленты
        if feed.status != 200:
            logger2.error('get_news_headlines: Error of loading RSS feed')
            return basic_output

        # Если загрузка RSS ленты прошла успешно, выводим заголовок
        news_list = []

        for item in feed.entries[0:n_news]:
            news_list.append({
                "title": item.title,
                "description": item.description,
                "img_url": item.links[1]["href"]
            })

        return news_list

    except Exception as e:
        logger2.error(f'get_news_headlines: {e}')
        await send_logs_auto(e)
        return basic_output
