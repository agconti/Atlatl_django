from django.conf.urls import patterns, url

from houses import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)