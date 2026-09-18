from django.views import generic


class IndexView(generic.TemplateView):
    """トップページ。WG のアプリに合わせて書き換える。"""

    template_name = 'core/index.html'
