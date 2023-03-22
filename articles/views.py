from django.shortcuts import render, HttpResponse
from articles.models import Article

# Create your views here.
def home(request):
    articles = Article.objects.order_by('-id')[:3]
    return render(request, 'articles/pages/home.html', context={
        'articles': articles
    })

def article(request, slug):
    article = Article.objects.filter(slug=slug).order_by('-id').first()
    return render(request, 'articles/pages/article-view.html', context={
        'article': article,
        'is_detail_page': True,
    })

def articlesList(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, 'articles/pages/article-list.html', context={
        'articles': articles
    })