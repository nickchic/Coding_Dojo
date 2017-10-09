from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/new', views.new_user_page),
    url(r'^add_user', views.add_user),
    url(r'^edit_user', views.edit_user),
    url(r'^users/(?P<id_num>[0-9])/$', views.user_page),
    url(r'^users/(?P<id_num>[0-9])/edit/', views.edit_user_page),
    url(r'^users/(?P<id_num>[0-9])/destroy/', views.destroy_user),
]
