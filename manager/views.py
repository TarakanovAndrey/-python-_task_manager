from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(selfr, request):
        return render(request, 'manager/index.html')
