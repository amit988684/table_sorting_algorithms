from django.conf.urls import url
# from django.contrib import admin
from .views import project_list

app_name = "company"

urlpatterns = [
    url(r'^$', project_list ,name="project_list"),
]