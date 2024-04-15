from django.shortcuts import render
from django.views.generic.base import TemplateView


class View(TemplateView):

    template_name = 'base.html'


def about(request):
    return render(request, 'about.html')
