from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext


class IndexView(View):

    def get(selfr, request):
        menu = ['Users', 'Login', 'Registration']
        project_name = 'Task manager'
        return render(request, 'manager/index.html', {'menu': menu, 'project_name': project_name})
