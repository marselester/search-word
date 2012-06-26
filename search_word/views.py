# -*- coding: utf-8 -*-
from django.shortcuts import render

from search_word.models import Article


def search(request):
    """Отображает список статей, в которых есть заданное слово."""
    desired_word = u'маркетинг'
    articles = Article.objects.filter(text__icontains=desired_word)
    return render(request, 'base.html', {
        'desired_word': desired_word,
        'articles': articles
    })
