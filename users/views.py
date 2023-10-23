from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from . forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy


def get_users_list(request):
    users_list = User.objects.all()
    return render(
        request,
        template_name='users/users_list.html',
        context={
            'users_list': users_list
        }
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


class LogoutUserView(LogoutView):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _('You are logged out'))
        return redirect('home')


class RegisterUserView(CreateView):

    def get(self, request, *args, **kwargs):
        form = RegisterUserForm()
        return render(
            request,
            template_name='users/create_user.html',
            context={
                'form': form,
                'title': _("Registration")
            }
        )

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(
                request,
                _('The user has been successfully registered'),
            )
            return redirect('login')
        return render(
            request,
            template_name='users/create_user.html',
            context={
                'form': form
            }
        )


class UserUpdateView(UpdateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('users_list')

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users_list')

    def form_valid(self, form):
        messages.success(self.request, 'OK')
        return super(UserDeleteView, self).form_valid(form)
