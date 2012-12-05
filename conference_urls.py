from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bowls.conference_views',
    url(r'^$', 'index'),
    url(r'^(?P<conference_id>\d+)/$', 'show'),
)
