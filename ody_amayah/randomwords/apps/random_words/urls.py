from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_words$', views.index),
    url(r'^generate$', views.generate),
]
