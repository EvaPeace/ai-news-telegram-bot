# AI News Telegram Bot


- [Russian ver.](#russian-ver)
  - [Информация о проекте "Новости от ИИ"](#информация-о-проекте-новости-от-ии)
  - [Информация о боте](#информация-о-боте)
    - [Технический стек](#технический-стек)
    - [Задачи бота](#задачи-бота)
  - [Лицензия](#лицензия)
  - [Контакты](#контакты)
- [English ver.](#english-ver)
  - [Information about the project "News from AI"](#information-about-the-project-news-from-ai)
  - [Bot information](#bot-information)
    - [Tech stack](#tech-stack)
    - [Bot tasks](#bot-tasks)
  - [License](#license)
  - [Contacts](#contacts)

# Russian ver.

English version [here](#English ver.) below

Это бот, который обращается к ChatGPT через OpenAI API, чтобы сгенерировать блок новостей и отправить его в Telegram канал [Новости от ИИ](https://t.me/NewsFromAIEvaPeace).

Этот репозиторий содержит код и информацию о проекте "Новости от ИИ", созданного в рамках школьного индивидуального проекта.

## Информация о проекте "Новости от ИИ"

- Это бизнес-план по школьному предмету индивидуальный проект.
- [Документ](https://docs.google.com/document/d/18fA1kwcifghY0xOPMk-2DYOgHAz882B37qK2h6nqXR0/edit?usp=sharing) с более официальным описанием и бизнес-планом проекта.

## Информация о боте

- Телеграм бот: [@evapeace_ai_news_telegram_bot](https://t.me/evapeace_ai_news_telegram_bot)
- Для обхода региональной блокировки OpenAI API используется [ProxyAPI](https://proxyapi.ru/)

### Технический стек

- **Язык:** Python
- **Фреймворк:** aiogram2
- **Библиотеки:** openai, [подробнее в requirements.txt](https://github.com/EvaPeace/ai-news-telegram-bot/blob/main/requirements.txt)

### Задачи бота

1. **Сбор новостей:**
   - Бот собирает актуальные новости с различных интернет-ресурсов.

2. **Генерация контента:**
   - Отправляет запрос к ChatGPT, чтобы получить пересказ собранных новостей.

3. **Регулярная отправка:**
   - В 7:00 и 18:00 по МСК бот отправляет новостные посты в Телеграм канал.

4. **Административная панель:**
   - Бот имеет административную панель, где можно выключить бота или изменить настройки.

## Лицензия

Код этого бота открыт и доступен на условиях [лицензии](https://github.com/EvaPeace/ai-news-telegram-bot/blob/main/LICENSE.md). Пожалуйста, обратите внимание, что использование бота в коммерческих целях запрещено.

## Контакты

Почта для связи: **damir.ernazarov.yesspeace@gmail.com**

# English ver.

This is a bot that accesses ChatGPT via the OpenAI API to generate a news block and send it to the Telegram channel [News from AI](https://t.me/NewsFromAIEvaPeace).

This repository contains code and information about the AI News project, created as part of a school individual project.

## Information about the project "News from AI"

- This is a business plan for a school subject, an individual project.
- [Document](https://docs.google.com/document/d/18fA1kwcifghY0xOPMk-2DYOgHAz882B37qK2h6nqXR0/edit?usp=sharing) with a more official description and business plan of the project.

## Bot information

- Telegram bot: [@evapeace_ai_news_telegram_bot](https://t.me/evapeace_ai_news_telegram_bot)
- To bypass regional blocking of OpenAI API, use [ProxyAPI](https://proxyapi.ru/)

### Tech stack

- **Language:** Python
- **Framework:** aiogram2
- **Libraries:** openai, [more details in requirements.txt](https://github.com/EvaPeace/ai-news-telegram-bot/blob/main/requirements.txt)

### Bot tasks

1. **News-gathering:**
    - The bot collects current news from various Internet resources.

2. **Content generation:**
    - Sends a request to ChatGPT to receive a retelling of the collected news.

3. **Regular dispatch:**
    - At 7:00 and 18:00 Moscow time, the bot sends news posts to the Telegram channel.

4. **Administrative panel:**
    - The bot has an administrative panel where you can turn off the bot or change settings.

## License

The code of this bot is open and available under the [license](https://github.com/EvaPeace/ai-news-telegram-bot/blob/main/LICENSE.md). Please note that using the bot for commercial purposes is prohibited.

## Contacts

Contact email: **damir.ernazarov.yesspeace@gmail.com**

