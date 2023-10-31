from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from . forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def get_home_page(request):
    return render(
        request,
        template_name='task_manager/index.html',
    )


class LoginUserView(LoginView):

    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(
            request,
            template_name='users/login.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, _('You are logged in'))
                return redirect('home')
            else:
                form = LoginUserForm(request.POST)
                messages.error(
                    request,
                    _('Please enter the correct username and password. '
                      'Both fields can be case sensitive.')
                )
                return render(
                    request,
                    template_name='users/login.html',
                    context={
                        'form': form,
                    }
                )


class LogoutUserView(SuccessMessageMixin, LogoutView):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _('You are logged out'))
        return redirect('home')
