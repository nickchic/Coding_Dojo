from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/course', views.add_course),
    url(r'^remove/(?P<id_num>[0-9]+)/confirm', views.remove_confirm),
    url(r'^remove/(?P<id_num>[0-9]+)', views.remove)
]
