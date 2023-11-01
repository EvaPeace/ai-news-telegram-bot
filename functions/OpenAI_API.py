import openai


def get_post_from_ChatGPT(news_headlines: list[str]) -> str:
    """
    Генерирует новостной пост на основе заданных заголовков новостей, обращаясь к ChatGPT через OpenAI API.

    :param news_headlines: Список заголовков новостей.
    :type news_headlines: list[str]
    :return: Новостной пост сгенерированный ChatGPT.
    :rtype: str
    """

    user_message = 'Привет, напиши провокационные, но короткие новостные статьи, примерно 100 слов, ' \
                   'по следующими заголовкам:\n '

    user_message = user_message + '\n'.join(news_headlines)

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": user_message}])

    chatgpt_answer = chat_completion["choices"][0]["message"]["content"]

    return chatgpt_answer
