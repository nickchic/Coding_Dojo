from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^users/(?P<user_id>[0-9]+)', views.user_page),
    url(r'^users/home', views.user_home),
    url(r'^$', views.main_book_page),
    url(r'^(?P<book_id>[0-9]+)', views.book_page),
    url(r'^add/review/(?P<book_id>[0-9]+)', views.add_review),
    url(r'^add$', views.add_page),
    url(r'^add/review_book', views.add_review_book)
]
