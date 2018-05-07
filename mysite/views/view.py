from django.shortcuts import render
from ..models.models import Article


def article_view(request):
    article = {
        'articles': Article.objects.order_by('id'),
    }
    return render(request, 'index.html', article)


def article_view2(request):
    article = {
        'articles': Article.objects.order_by('id'),
    }
    return render(request, 'article.html', article)
