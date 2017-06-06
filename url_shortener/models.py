from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=settings.SHORTENED_LENGTH, db_index=True)
