from django.conf.urls import patterns, include, url
from watchapp import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^constructora_home/$', views.constructora_home, name='constructora_home'),
    url(r'^users_home/$', views.users_home, name='users_home'),
    url(r'^login/$', login, {'template_name': 'watchapp/login.html', }, name="login"),
	url(r'^login_success/$', views.login_success, name='login_success'),
	url(r'^accounts/login$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout, {'template_name': 'watchapp/login.html', }, name="logout"),
	url('', include('django.contrib.auth.urls')),
	
	url(r'^get_property_info_by_name/', views.get_property_info_by_name, name='get_property_info_by_name'),
)