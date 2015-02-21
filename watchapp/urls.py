from django.conf.urls import patterns, include, url
from watchapp import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'watchapp/login.html', }, name="login"),
	url(r'^accounts/login$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout, {'template_name': 'watchapp/login.html', }, name="logout"),
	url('', include('django.contrib.auth.urls')),
)