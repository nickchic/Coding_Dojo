from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^login_action$', views.login_action),
    url(r'^register_action$', views.register_action)
]
