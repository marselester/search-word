# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def highlight(text, word):
    return mark_safe(text.replace(word, '<b style="color:red">%s</b>' % word))


@register.filter
def truncate_near_word(text, word, width=200):
    head, word, tail = text.partition(word)
    return head[-width:] + word + tail[:width]
