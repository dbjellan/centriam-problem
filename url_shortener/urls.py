from django.conf.urls import url
from django.conf import settings

from . import views

shortened_url_regex = r'^[0-9a-zA-Z]{%s}' % (settings.SHORTENED_LENGTH)

urlpatterns = [
    url(shortened_url_regex, views.shortened_url),
    url(r'^new', views.new_url),
    url(r'^$', views.index)
]
