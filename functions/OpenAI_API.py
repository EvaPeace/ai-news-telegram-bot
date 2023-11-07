import logging

import openai

# настройка базового логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (может быть DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(name)s %(asctime)s %(levelname)s %(message)s",
    filename='main_log.log',  # Имя файла, куда будут записываться логи
    filemode='a+',  # Режим записи (a - добавление, w - перезапись)
    encoding='utf-8'
)

logger2 = logging.getLogger(__name__)


def get_post_from_ChatGPT(news_headlines: list[str]) -> str | None:
    """
    Генерирует новостной пост на основе заданных заголовков новостей, обращаясь к ChatGPT через OpenAI API.
    В случае ошибки возвращает None

    :param news_headlines: Список заголовков новостей.
    :type news_headlines: list[str]
    :return: Новостной пост сгенерированный ChatGPT (str) или None в случе ошибки
    :rtype: str | None
    """
    try:
        user_message = 'Привет, напиши провокационные, но короткие новостные статьи, примерно 100 слов, ' \
                       'по следующими заголовкам:\n'

        user_message = user_message + '\n'.join(news_headlines)

        message = {"role": "user", "content": user_message}

        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[message])

        chatgpt_answer = chat_completion["choices"][0]["message"]["content"]

        log_dict = {
            "input_data": news_headlines,
            "user_message": user_message,
            "chatgpt_answer": chat_completion,
            "output_data": chatgpt_answer,
        }

        logger2.info('get_post_from_ChatGPT' + str(log_dict))

        return chatgpt_answer

    except TypeError as e:
        logger2.error(f"get_post_from_ChatGPT - Incorrect input data type in news_headlines: {e}")

    except openai.error.OpenAIError as e:
        # Handle timeout error, e.g. retry or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API: {e}")
