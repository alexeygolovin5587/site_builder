from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Html(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'tbl_html'

class MasterTemplate(models.Model):
    name = models.CharField(max_length=255)
    img_path = models.CharField(max_length=255)
    html_path = models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_master'

class Module(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    content = models.TextField(default="")

    added = models.BooleanField(default=False)

    master = models.ForeignKey(MasterTemplate, default=1)
    class Meta:
        db_table = 'tbl_module'