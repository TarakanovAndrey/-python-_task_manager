from django.shortcuts import render
from django.views import View
from . forms import CustomUserCreationForm
from django.utils.translation import gettext_lazy


class CustomUserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm
        return render(request, 'users/create_user.html', {'form': form})

    def post(self, request):
        pass


class UsersListView(View):

    def get(self, request):
        return render(request, 'users/users_list.html', {'users_list': [{'id': 1, 'nickname': 'SmallNiels', 'full_name': 'Andrey Tarakanov', 'created_at': '23.34.34'}]})