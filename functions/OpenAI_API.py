import config

import logging

import openai

logger2 = logging.getLogger(__name__)


def get_post_from_ChatGPT(news_headlines: list[str]) -> str:
    """
    Генерирует новостной пост на основе заданных заголовков новостей, обращаясь к ChatGPT через OpenAI API.
    В случае ошибки возвращает None

    :param news_headlines: Список заголовков новостей.
    :type news_headlines: list[str]
    :return: Новостной пост сгенерированный ChatGPT.
    :rtype: str
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

    except openai.error.Timeout as e:
        # Handle timeout error, e.g. retry or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API request timed out: {e}")

    except openai.error.APIError as e:
        # Handle API error, e.g. retry or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API returned an API Error: {e}")

    except openai.error.APIConnectionError as e:
        # Handle connection error, e.g. check network or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API request failed to connect: {e}")

    except openai.error.InvalidRequestError as e:
        # Handle invalid request error, e.g. validate parameters or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API request was invalid: {e}")

    except openai.error.AuthenticationError as e:
        # Handle authentication error, e.g. check credentials or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API request was not authorized: {e}")

    except openai.error.PermissionError as e:
        # Handle permission error, e.g. check scope or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API request was not permitted: {e}")

    except openai.error.RateLimitError as e:
        # Handle rate limit error, e.g. wait or log
        logger2.error(f"get_post_from_ChatGPT - OpenAI API request exceeded rate limit: {e}")
