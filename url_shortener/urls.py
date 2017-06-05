from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^[0-9a-zA-Z]{6}', views.shortened_url),
    url(r'^new', views.new_url),
    url(r'^$', views.index)
]
