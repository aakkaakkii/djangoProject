from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from ..models.models import Article
from ..forms import NameForm

from django.http import HttpResponse
from django.http import JsonResponse


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


@login_required(login_url='/login/')
def add_article(request):
    return render(request, 'article-add-page.html', {})


def get_data(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        some = {
            'text': 'ayy lmao',
        }
        article_obj = Article(title=form['title'].value(), text=form['text'].value())
        article_obj.save()

        return render(request, 'some.html', some)

    return render(request, 'some.html', {'title': '12341234'})


@login_required(login_url='/login/')
def remove_data(request):
    article = {
        'articles': Article.objects.order_by('id'),
    }
    return render(request, 'article-remove.html', article)


def remove(request):
    if request.method == 'POST':
        Article.objects.get(id=int(request.POST["article_id"])).delete()
    return HttpResponse('asd')


def load_data(request):
    result = {}
    if request.method == 'POST':
        post_id = int(request.POST["post_id"])
        if post_id < Article.objects.all().__len__():
            result = {
                "id": Article.objects.all()[post_id:post_id+1].values()[0]['id'],
                "title": Article.objects.all()[post_id:post_id+1].values()[0]['title'],
                "text": Article.objects.all()[post_id:post_id+1].values()[0]['text']
            }
    return JsonResponse(result)
