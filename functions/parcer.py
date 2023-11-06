import feedparser


def get_news_headlines(n_news=3, url='https://motor.ru/exports/rss') -> list[str]:
    """
    Получает список заголовков новостей и возвращает его как список строк (str).

    :param url:
    :type url: str
    :param n_news: Количество новостей для получения.
    :type n_news: int
    :return: Список заголовков новостей в виде списка строк (str).
    :rtype: list[str]
    """

    # Создаем объект feedparser для работы с RSS лентой
    feed = feedparser.parse(url)

    # Проверяем успешность загрузки RSS ленты
    if feed.status != 200:
        print("Ошибка загрузки RSS ленты")
        return

    # Если загрузка RSS ленты прошла успешно, выводим заголовок
    Titles_list = []
    for item in feed.entries:
        Titles_list.append(item.title)
    Three_First_News = Titles_list[0:3:1]
    return Three_First_News
