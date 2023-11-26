import logging
import os

from functions import send_logs_auto

logger = logging.getLogger(__name__)


async def check_logs_size_and_delete(logs_file_path: str, max_size_bytes=1 * 1024 * 1024) -> None:
    """
    Проверяет размер файла логгов и, если размер больше максимального, удаляет его.

    :param logs_file_path: Путь, по которому, расположен файл логгов.
    :param max_size_bytes: Максимальный допустимый размер файла логгов. По умолчанию 1МБ в байтах.
    :return: None
    """

    try:
        file_size_bytes = os.path.getsize(logs_file_path)

        if file_size_bytes > max_size_bytes:
            os.remove(logs_file_path)
            logger.info(f"check_logs: The file {logs_file_path} deleted, "
                        f"because it's bigger than {max_size_bytes} in bytes.")

        else:
            logger.info(f"check_logs: Logs file's size checked. Nothing changed.")

    except (FileNotFoundError, PermissionError) as e:
        logger.error(f'check_logs: The file {logs_file_path} does not exist.')
        await send_logs_auto(e)

    except Exception as e:
        logger.error(f"check_logs {e}")
        await send_logs_auto(e)
