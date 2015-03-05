from django.conf.urls import patterns, include, url
from watchapp import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    #URLs index o para autenticacion
	url(r'^$', TemplateView.as_view(template_name='watchapp/index.html')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, {'template_name': 'watchapp/login.html', }, name="login"),
	url(r'^login_success/$', views.login_success, name='login_success'),
    url(r'^logout/$', logout, {'template_name': 'watchapp/login.html', }, name="logout"),
	url(r'^sensorstatus/$', views.get_PropertysByUser, name='get_PropertysByUser'),
	url('', include('django.contrib.auth.urls')),
	
	#URLs para funcionalidades de usuarios (residente/propietario)
    url(r'^users_home/$', views.users_home, name='users_home'),
	
	#URLs para funcionalidades de constructoras    
	url(r'^constructora_home/$', views.constructora_home, name='constructora_home'),

)
