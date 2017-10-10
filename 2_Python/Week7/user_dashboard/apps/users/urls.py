from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login_page),
    url(r'^login_action$', views.login_action),
    url(r'^register$', views.register_page),
    url(r'^register_action$', views.register_action),
    url(r'^users/new$', views.new_user_page),
    url(r'^users/new_action$', views.new_user_action),
    url(r'^users/show/(?P<user_id>[0-9]+)', views.user_page),
    url(r'^dashboard$', views.user_dashboard),
    url(r'^dashboard/admin$', views.admin_dashboard),
    url(r'^users/edit$', views.edit_user_page),
    url(r'^users/edit/(?P<user_id>[0-9]+)$', views.edit_admin_page),
    url(r'^users/edit_action/(?P<user_id>[0-9]+)$', views.edit_action),
    url(r'^users/remove/(?P<user_id>[0-9]+)$', views.remove_user),
    url(r'^post_message/(?P<user_id>[0-9]+)$', views.post_message),
    url(r'^post_comment/(?P<user_id>[0-9]+)/(?P<message_id>[0-9]+)', views.post_comment)
]
