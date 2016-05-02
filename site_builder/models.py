from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Html(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'tbl_html'

class NewTheme(models.Model):
    url = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_theme'