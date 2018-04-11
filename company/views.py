# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.views.generic import ListView,FormView
from .models import Project
from .forms import OrderingListForm
from django.shortcuts import redirect

from .tables import ProjectTable
# Create your views here.
from django_tables2 import RequestConfig



def project_list(request):
    queryset = Project.objects.all()
    table = ProjectTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'company/project_list.html', {'table': table})





# class ProjectView(ListView,FormView):
#     model = Project
#     form_class = OrderingListForm
#
#     def get_queryset(self):
#         return Project.objects.all()
#
#     def form_valid(self, form):
#         order_list = form.cleaned_data
#         order_list = str(order_list['ordering_list'])
#         print (order_list)
#
#         return redirect('company:project_list')