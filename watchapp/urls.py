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
    url(r'^get_owner_reports/$', views.get_owner_reports, name='get_owner_reports'),
    url(r'^(?P<property_id>\d+)(?P<asresident>[a-zA-Z0-9]+)/change_secure_mode/$', views.change_secure_mode, name='change_secure_mode'),
	#URLs para funcionalidades de usuarios (residente/propietario)
    url(r'^users_home/$', views.users_home, name='users_home'),
    url(r'^sensor_configuration/$', views.sensor_configuration, name='sensor_configuration'),
	url(r'^update_sensor/$', views.update_sensor, name='update_sensor'),
	#URLs para funcionalidades de constructoras    
	url(r'^constructora_home/$', views.constructora_home, name='constructora_home'),
	#URL para crear un sensor en un plano
    url(r'^set_position_ajax/$', views.set_position_ajax, name='set_position_ajax'),
	#URL para eliminar un sensor en un plano
    url(r'^delete_position_ajax/$', views.delete_position_ajax, name='delete_position_ajax'),
    url('', include('django.contrib.auth.urls')),
    #url(r'^rpt_admin_property/$', views.rpt_admin_property, name='rpt_admin_property'),
    # URL- Reporte de eventos de los inmuebles de un propietario
    url(r'^rpt_owner_property/$', views.rpt_owner_property, name='rpt_owner_property'),
    # URL para generar en PDF el reporte de eventos de los inmuebles de un propietario
    url(r'^get_report_owner_property/$', views.get_report_owner_property, name='get_report_owner_property'),
    url(r'^get_report_admin_all_property/$', views.get_report_admin_all_property, name='get_report_admin_all_property'),
    # URL para consultar los datos del reporte de eventos de los inmuebles de un propietario
    url(r'^get_event_owner_property/$', views.get_event_owner_property, name='get_event_owner_property'),
    url(r'^get_event_admin_all_property/$', views.get_event_admin_all_property, name='get_event_admin_all_property'),
    url(r'^rpt_admin_all_property/$', views.rpt_admin_all_property, name='rpt_admin_all_property'),
    #url(r'^admin_file_upload/$', views.admin_file_upload, name='admin_file_upload'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
)
