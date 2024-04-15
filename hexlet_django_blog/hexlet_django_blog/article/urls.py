from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    #path('', views.ArticlesView.as_view()),
    path('<str:tags>/<int:article_id>/', views.index, name='articles'),
    path('', views.home, name='home')
]
