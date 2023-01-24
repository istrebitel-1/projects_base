import logging
import os

from backend.core.constants import ApplicationMode


def configure_application():
    def show_debug_message():
        print("! THE APP IS RUNNING WITH DEBUG MODE")

    def configure_logging():
        root_logger = logging.getLogger()

        # If logger exists
        if root_logger.handlers:
            return

        log_level = os.getenv('APP_LOG_LEVEL', 'INFO')
        root_logger.setLevel(log_level)

        formatter = logging.Formatter(
            fmt="[%(asctime)s] - %(levelname)s - %(process)d - %(name)s:%(lineno)d: %(message)s",
            datefmt="%d.%m.%Y %H:%M:%S"
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

        containerized = os.getenv('APP_CONTAINERIZED', 'false').lower() == 'true'
        if not containerized:
            log_path = os.environ['APP_LOG_PATH']
            os.makedirs(log_path, exist_ok=True)

            file_handler = logging.FileHandler(
                filename=os.path.join(log_path, 'app.log'),
                encoding="utf-8"
            )
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)

        logging.getLogger('urllib3').setLevel(logging.WARNING)

    app_mode = os.getenv('APP_MODE', ApplicationMode.LOCAL)
    debug = app_mode == ApplicationMode.LOCAL
    if debug:
        show_debug_message()

    if app_mode == ApplicationMode.LOCAL:
        ...
        from backend.config.environment.local import apply_local_env
        apply_local_env()

    configure_logging()
