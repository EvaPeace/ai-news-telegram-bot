import feedparser


def parse_rss(url='https://motor.ru/exports/rss'):
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
