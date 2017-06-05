from __future__ import unicode_literals

from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=6)
