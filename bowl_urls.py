from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bowls.bowl_views',
    url(r'^$', 'index'),
    url(r'^(?P<bowl_id>\d+)/$', 'show'),
)
