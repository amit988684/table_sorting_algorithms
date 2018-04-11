# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
    distance = models.IntegerField()
    rate = models.IntegerField()
    project_size = models.IntegerField()
    completion_date = models.DateField(null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ['pk']