from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from django.views import generic


# 本番は既定で全ビューがログイン必須（homepage の LoginRequiredMiddleware）。
# 誰でも見られるページには login_not_required を付けて外す。付け忘れると、
# 手元では見えるのに公開したらログイン画面に飛ばされる。
@method_decorator(login_not_required, name='dispatch')
class IndexView(generic.TemplateView):
    """トップページ。WG のアプリに合わせて書き換える。"""

    template_name = 'core/index.html'
