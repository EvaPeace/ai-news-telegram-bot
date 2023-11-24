import feedparser


def get_news_headlines(n_news=3, url='https://news.rambler.ru/rss/politics/') -> list[str] | None:
    """
    Получает список заголовков новостей и возвращает его как список строк (str).

    :param url:
    :type url: str
    :param n_news: Количество новостей для получения.
    :type n_news: int
    :return: Список заголовков новостей в виде списка строк (str) или None в случае ошибки
    :rtype: list[str] | None
    """

    # Создаем объект feedparser для работы с RSS лентой
    feed = feedparser.parse(url)

    # Проверяем успешность загрузки RSS ленты
    if feed.status != 200:
        print("Ошибка загрузки RSS ленты")
        return

    # Если загрузка RSS ленты прошла успешно, выводим заголовок
    titles_list = []

    for item in feed.entries:
        titles_list.append(item.title)

    three_first_news = titles_list[0:3:1]

    return three_first_news
