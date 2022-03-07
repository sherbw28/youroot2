import os

#settings.pyからそのままコピー
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-72el(^+66^crh0wbs5#*#@o3cft^=2hs-29zmuya(i958i5h^f' # settings.py から該当部分コピー

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True