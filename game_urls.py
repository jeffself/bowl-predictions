from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bowls.game_views',
    url(r'^$', 'index'),
    url(r'^(?P<game_id>\d+)/$', 'show'),
)
