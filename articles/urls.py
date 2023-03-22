from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="articles-home"),
    path('artigos/', views.articlesList, name="articles-list"),
    path('artigo/<slug:slug>', views.article, name="articles-article"),
    
]
