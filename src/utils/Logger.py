import logging
from functools import wraps
from threading import Lock
from typing import Any, Optional, Callable


class Singleton(type):
    _instances = {}
    _lock = Lock()  # Ensure thread safety

    def __call__(cls, *args, **kwargs) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self):
        self.root_logger = logging.getLogger()
        self.__configure()

    def __configure(self):
        #root_logger = logging.getLogger()

        # Remove all existing handlers
        for handler in self.root_logger.handlers[:]:
            self.root_logger.removeHandler(handler)

        # Now add a fresh StreamHandler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s -- %(message)s -- ROOT LOGGER"
        ))

        self.root_logger.addHandler(console_handler)
        self.root_logger.setLevel(logging.INFO)

    def getLogger(self):
        return self.root_logger



def log(func: Optional[Callable] = None) -> Callable:
    logger_instance = Logger() # Get the singleton instance of Logger
    logger = logger_instance.getLogger()

    def decorator(inner_func: Callable) -> Callable:
        @wraps(inner_func)
        def wrapper(self, *args, **kwargs) -> Any:
            log_message = ( f" Method :: {func.__name__}() with parameters: {args}")
            logger.info(log_message)
            return func(self, *args, **kwargs)

        return wrapper

    if callable(func):
        return decorator(func)

    return decorator


