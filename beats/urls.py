from django.conf.urls import patterns, url
from beats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)