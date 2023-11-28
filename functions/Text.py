import logging

import openai

from config import admins_ids, bot

logger2 = logging.getLogger(__name__)


async def get_post_from_ChatGPT(news_headlines: list[str]) -> str | None:
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
        await send_logs_auto(e)

    except openai.error.OpenAIError as e:
        # Handle timeout error, e.g. retry or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API: {e}")
        await send_logs_auto(e)

    except Exception as e:
        logger2.error(f"get_post_from_ChatGPT: {e}")
        await send_logs_auto(e)

async def send_logs_auto(exception: Exception):
    """
    Автоматически отправляет логги в лс всех админов, при каких-либо ошибках.
    Логги админов храняться в перменой admins_ids в config.py и берутся из переменных окружения.

    :param exception: Ошибка, которая вынудила вызвать функцию.
    :type exception: Exception
    """
    with open('.\main_log.log', 'rb') as log_file:
        for admin_id in admins_ids:
            await bot.send_message(
                chat_id=admin_id,
                text='Внимание! Случилась какая-то ошибка. Высылаю логги.\n\n'
                     'Логги высланы по вине следующей ошибки:\n\n' + str(exception)
            )

            await bot.send_document(
                chat_id=admin_id,
                document=log_file
            )
