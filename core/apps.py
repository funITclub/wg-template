from django.apps import AppConfig

# このアプリは、WG ごとに一意な名前へ変えてから中身を作る（例: protein）。
# 公開のときは、このフォルダーごと homepage の wg/ へ移すため（README の「公開」）。


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'アプリ'
