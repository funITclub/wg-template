# config/settings_dev.py — ローカル開発用

import os

from .settings_common import *

# ローカルの秘密情報は .env から読む（.gitignore 済み）。
# 既に環境変数がある場合はそちらを優先する（setdefault）。
_env_file = BASE_DIR / '.env'
if _env_file.exists():
    for _line in _env_file.read_text(encoding='utf-8').splitlines():
        _line = _line.strip()
        if not _line or _line.startswith('#') or '=' not in _line:
            continue
        _key, _value = _line.split('=', 1)
        os.environ.setdefault(_key.strip(), _value.strip().strip('\'"'))

SECRET_KEY = 'django-insecure-funitclub-wg-local-development-key'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
CSRF_TRUSTED_ORIGINS = []

# メールは送らず、runserver のログに出す。
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
