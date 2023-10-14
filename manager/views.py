from django.shortcuts import render
from django.views import View
from django.middleware.csrf import  get_token



class IndexView(View):

    def get(selfr, request):
        return render(request, 'manager/index.html')



class LoginView(View):

    def get(self, request):
        csrf_token = get_token(request)
        return render(request, 'manager/login.html', {'csrf_token': csrf_token})


    def post(self, request):
        pass



