from django.conf.urls import url
from .  import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^load_notes$', views.load_notes),
    url(r'^add$', views.add),
    url(r'^add_text', views.add_text),
    url(r'^delete/(?P<note_id>[0-9]+)', views.delete)
]
