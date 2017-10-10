from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^reg', views.register),
    url(r'^success', views.success),
    url(r'^login$', views.login_page),
    url(r'^login_attempt', views.login),
    url(r'^', views.index)
]
