from django.db.models import Prefetch
from django.shortcuts import render

from articles.models import Article, ArticleScope, Tag


def articles_list(request):

    template = 'articles/news.html'
    object_list = Article.objects.all().prefetch_related('scopes')
    context = {'object_list': object_list}


    return render(request, template, context)
