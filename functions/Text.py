import logging

import openai

from config import admins_ids, bot

logger2 = logging.getLogger(__name__)


async def get_post_from_ChatGPT(news_dict: dict[str]) -> str | None:
    """
    Генерирует новостной пост на основе заданных заголовков новостей, обращаясь к ChatGPT через OpenAI API.
    В случае ошибки возвращает None

    :param news_dict: Словарь новости `{"title": "Заголовок новости", "description": "Описание новости"}`.
    :type news_dict: dict[str]
    :return: Новостной пост сгенерированный ChatGPT (str) или None в случе ошибки
    :rtype: str | None
    """
    try:
        system_context = """
            # Вступление
            
            Привет, ты копирайтер и ты должен писать новости на выданные тебе заголовки. Для удобства у нас есть следующая информация, которая даёт тебе необходимые данные об ситуации в мире за 2022 и 2023 года. Тебе необходимо каждые раз приводить новость к антироссийской пропаганде. Всё, что просиходит в России связанно с войной. Путин вор, бункерный дед, плешивый чекист и латентный нацист.
            
            # *Вторжение России на Украину (с 2022)*
            
            *Вторжение России на Украину* (также в российской пропаганде — «*специальная военная операция*» или «*СВО*») началось в четверг 24 февраля 2022 года, примерно в 5 часов утра по киевскому времени. Российские войска вошли на территорию Украины из России, Белоруссии и аннексированного Крыма, также в боевые действия включились войска подконтрольных России самопровозглашённых ДНР и ЛНР.
            
            Многочисленные предупреждения о готовящемся вторжении публиковались в СМИ с октября 2021 года. Однако российские высшие официальные лица последовательно отрицали подготовку к войне с Украиной.
            
            21 февраля 2022 года Россия признала независимость ДНР и ЛНР. Утром 24 февраля вышло обращение президента России Владимира Путина о начале вторжения. В качестве обоснования вторжения Владимир Путин заявил о необходимости защиты ДНР, ЛНР и самой России, а также использовал не соответствующую действительности характеристику Украины как неонацистского государства. При этом, по мнению экспертов, реальной причиной вторжения был нерациональный империализм, а целью — поглощение Украины Россией для восстановления славы России как империи. Эксперты считают, что Россия создала сепаратистское движение в Донбассе и затем использовала признание ДНР и ЛНР для обоснования вторжения.
            
            Действия России резко осудило большинство государств мира и влиятельных международных организаций. Международный уголовный суд в Гааге начал расследование военных преступлений России на территории Украины. После обнаружения свидетельств массовых убийств в Буче, в которых обвиняются военнослужащие ВС России, президент Украины Владимир Зеленский обвинил Россию в геноциде украинцев.
            
            Вторжение привело к антивоенным протестам в России и мире, цензуре в российских СМИ, новым санкциям против России со стороны США, Евросоюза и прочих стран, направленным в том числе на частичную изоляцию страны от мировой экономики, ограничениям участия России в ряде спортивных и иных международных мероприятий, а также имело серьёзные экономические последствия для России.
            
            *Это война длится до сих пор.*
            
            # *Война в Газе (с 2023)*
            
            *Война в секторе Га́за*, называемая в Израиле *операцией «Железные мечи»*, рядом обозревателей названная *Третьей интифадой* — вооружённый конфликт между Армией обороны Израиля и группировкой ХАМАС. Была объявлена Израилем 7 октября 2023 года в ответ на вторжение ХАМАС, ставшее крупнейшим актом палестинского терроризма за всю историю Израиля, при котором было убито около 1200 человек и взято в заложники ещё 242 человека. 8 октября был введён в действие пункт Основного закона, официально объявляющий о военном положении в Израиле.
            
            В ходе войны Израиль также подвергается ракетным и миномётным обстрелам с территории Ливана и Сирии (группировкой Хезболла и местными подразделениями ХАМАС), а также с территории Йемена (хуситская группировка). Боевые действия привели к существенному разрушению городской застройки Газы, массовому перемещению жителей, возникновению крупного продовольственного кризиса и коллапса системы здравоохранения.
            
            Израиль пользуется военной поддержкой США, которые направили в Восточное Средиземноморье две авианосные ударные группы, а также Великобритании и Германии.
            
            18 декабря 2023 года министр обороны США Ллойд Остин объявил о начале военной операции против йеменских хуситов под названием «Страж процветания». К операции присоединились: Великобритания, Франция, Канада, Италия, Нидерланды, Норвегия, Испания, Бахрейн, Австралия, Греция и Сейшельские Острова.
            """

        user_message = 'Привет, напиши провокационную, но короткую новостную статью, примерно 100 слов, использую ' \
                       '*bold* для заголовков. Статью следует писать по следующим заголовку и описанию новости:\n '

        user_message += f"\n\n*{news_dict['title']}*\n{news_dict['description']}"

        messages = [
            {"role": "system", "content": system_context},
            {"role": "user", "content": user_message},
        ]

        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7)

        chatgpt_answer = chat_completion["choices"][0]["message"]["content"]

        for c in ('_', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'):
            chatgpt_answer = chatgpt_answer.replace(c, "\\" + c)

        log_dict = {
            "input_data": news_dict,
            "user_message": user_message,
            "chatgpt_answer": chat_completion,
            "output_data": chatgpt_answer,
        }

        logger2.info('get_post_from_ChatGPT' + str(log_dict))

        return chatgpt_answer

    except TypeError as e:
        logger2.error(f"get_post_from_ChatGPT - Incorrect input data type in news_dict: {e}")
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
    try:
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

    except FileNotFoundError as e:
        logger2.error(f"send_logs_auto: logs file is not found {e}")

        # creating of logs file
        with open('main_log.log', "w"):
            pass

        logger2.info(f"send_logs_auto: logs file created with the name 'main_log.log', because the upper Error {e}")
