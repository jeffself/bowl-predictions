from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bowls.school_views',
    url(r'^$', 'index'),
    url(r'^(?P<school_id>\d+)/$', 'show'),
)
