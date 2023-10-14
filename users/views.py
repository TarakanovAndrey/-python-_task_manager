from django.shortcuts import render, redirect
from django.views import View
from . forms import CustomUserCreationForm, UserLoginForm
from django.utils.translation import gettext_lazy as _
from django.middleware.csrf import  get_token


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        pass


class LogoutView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class CustomUserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm
        return render(request, 'users/create_user.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'users/create_user.html', {'form': form})


class UsersListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/users_list.html', {'users_list': [{'id': 1, 'nickname': 'SmallNiels', 'full_name': 'Andrey Tarakanov', 'created_at': '23.34.34'}]})
