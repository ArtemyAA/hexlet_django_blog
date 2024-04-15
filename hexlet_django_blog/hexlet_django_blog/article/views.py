from hexlet_django_blog.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.


class ArticlesView(View):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'article'
        return context


def index(request, tags, article_id):
    article_text = f'Это статья номер {article_id}, по тегу {tags}'
    return render(
        request,
        'articles/index.html',
        {'article_text': article_text})


def home(request):
    article_url = reverse('articles', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(article_url)