# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('distance','rate','project_size','completion_date')

admin.site.register(Project,ProjectAdmin)