from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),     # This line has changed!
  url(r'^new$', views.index),    # This line has changed!
  url(r'^create$', views.create),    # This line has changed!
  url(r'^(?P<blog_id>\d+)$', views.route_param)
  # url(r'^(?P<blog_id>\d+)/show$', views.show)
  # url(r'^(?P<blog_id>\d+)/edit$', views.edit)
  # url(r'^(?P<blog_id>\d+)/delete$', views.delete)
]
