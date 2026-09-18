# config/settings.py — 本番用
#
# 公開（デプロイ）の仕組みは準備中。値はすべて環境変数から読み、リポジトリには持たない。

import os

from .settings_common import *

SECRET_KEY = os.environ['SECRET_KEY']

# 既定は False。切り分けが必要なときだけ一時的に DEBUG=True にし、済んだら必ず戻す。
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# 公開するホスト名をカンマ区切りで渡す（例: ALLOWED_HOSTS=wg-example.funitclub.org）。
ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',') if h.strip()]
CSRF_TRUSTED_ORIGINS = [f'https://{h}' for h in ALLOWED_HOSTS]

# 静的ファイルは WhiteNoise で配信する。
idx = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
MIDDLEWARE.insert(idx + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# HTTPS はフロント（ロードバランサー）で終端し、X-Forwarded-Proto で転送される想定。
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
