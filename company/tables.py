from .models import Project
import django_tables2 as tables


class ProjectTable(tables.Table):
    class Meta:
        model = Project
        template_name = 'django_tables2/bootstrap.html'


        # attrs = {'table': {'class': 'table'},'thead':{'thead-dark'},'th':{'scope':'col'} }