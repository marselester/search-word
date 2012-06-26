# -*- coding: utf-8 -*-
from django.shortcuts import render

from search_word.models import Article


def search(request):
    """Отображает список статей, в которых есть заданное слово."""
    desired_word = u'взгляд'
    articles = Article.objects.filter(text__icontains=desired_word)
    for article in articles:
        head, word, tail = article.text.partition(desired_word)
        article.truncated_text = head[-200:] + desired_word + tail[:200]
    return render(request, 'base.html', {'articles': articles})
