import logging

import openai

logger2 = logging.getLogger(__name__)


def get_post_from_ChatGPT(news_headlines: list[str]) -> str:
    """
    Генерирует новостной пост на основе заданных заголовков новостей, обращаясь к ChatGPT через OpenAI API.

    :param news_headlines: Список заголовков новостей.
    :type news_headlines: list[str]
    :return: Новостной пост сгенерированный ChatGPT.
    :rtype: str
    """

    user_message = 'Привет, напиши провокационные, но короткие новостные статьи, примерно 100 слов, ' \
                   'по следующими заголовкам:\n'

    user_message = user_message + '\n'.join(news_headlines)
    message = {"role": "user", "content": user_message}

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[message])

    chatgpt_answer = chat_completion["choices"][0]["message"]["content"]

    logger2.info(f'\nget_post_from_ChatGPT[\n'
                 f'    "input_data": {news_headlines},\n'
                 f'    "output_data": {chatgpt_answer}\n'
                 f']')

    logger2.info(f'\nget_post_from_ChatGPT[\n'
                 f'    "user_message": "{user_message}",\n'
                 f'    "chatgpt_answer": {chat_completion}\n'
                 f']')

    return chatgpt_answer
