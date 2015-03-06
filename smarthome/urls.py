from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from watchapp import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
urlpatterns = [
    url(r'^watchapp/', include('watchapp.urls', namespace="watchapp")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]