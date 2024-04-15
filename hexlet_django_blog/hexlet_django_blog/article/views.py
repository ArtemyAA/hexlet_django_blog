from hexlet_django_blog.views import View
# Create your views here.


class ArticlesView(View):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'article'
        return context
