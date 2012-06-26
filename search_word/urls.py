from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('search_word.views',
    url(r'^$', 'search', name='search_word'),
)
