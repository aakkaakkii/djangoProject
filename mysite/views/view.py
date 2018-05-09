from django.shortcuts import render
from ..models.models import Article

from ..forms import NameForm


def article_view(request):
    article = {
        'articles': Article.objects.order_by('id'),
    }
    return render(request, 'index.html', article)


def article_view2(request, article_id):
    article = {
        'articles': Article.objects.get(id=article_id),
    }
    return render(request, 'article.html', article)


def add_article(request):
    return render(request, 'article-add-page.html', {})


def get_data(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        some = {
            'title': form['title'].value(),
            'text': form['text'].value(),

        }
        return render(request, 'some.html', some)

    return render(request, 'some.html', {'title': '12341234'})
