import os
import logging

DEBUG = True if os.environ.get('DEBUG', 'false').lower() == 'true' else False
LOG_LEVEL = logging.DEBUG if DEBUG is True else logging.INFO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
    'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
]
