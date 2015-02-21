from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^watchapp/', include('watchapp.urls', namespace="watchapp")),
    url(r'^admin/', include(admin.site.urls)),
]