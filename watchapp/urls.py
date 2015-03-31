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
	url(r'^sensorstatus/$', views.render_sensor_status, name='render_sensor_status'),
    url(r'^(?P<property_id>\d+)/change_secure_mode/$', views.change_secure_mode, name='change_secure_mode'),
	url('', include('django.contrib.auth.urls')),
	
	#URLs para funcionalidades de usuarios (residente/propietario)
    url(r'^users_home/$', views.users_home, name='users_home'),
url(r'^sensor_configuration/$', views.sensor_configuration, name='sensor_configuration'),
	#URLs para funcionalidades de constructoras    
	url(r'^constructora_home/$', views.constructora_home, name='constructora_home'),

)
