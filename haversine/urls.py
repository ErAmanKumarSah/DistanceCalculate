from django.conf.urls import url
from django.contrib import admin

from haversine.db import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^haversine/', include('haversine.url')),
	url(r'^admin/', include(admin.site.urls)),
]
