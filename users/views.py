from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from . forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users_list'


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('login')
    success_message = _("The user has been successfully registered")


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





class UserUpdateView(UpdateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('users_list')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _("You are not logged in! Please log in."))
            return redirect('login')

        user_id_for_update = kwargs['pk']
        user_id_auth = self.request.user.id

        if user_id_for_update != user_id_auth:
            messages.error(self.request, _("You don't have the rights to change another user."))
            return redirect('users_list')

        form = RegisterUserForm(instance=request.user)
        return render(request, 'users/user_update.html', {'form': form})

    def form_valid(self, form):
        messages.success(self.request, _('User successfully changed'))
        return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users_list')

    # def get(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         messages.error(self.request, _("You are not logged in! Please log in."))
    #         return redirect('login')
    #
    #     user_id_for_delete = kwargs['pk']
    #     user_id_auth = self.request.user.id
    #
    #     if user_id_for_delete != user_id_auth:
    #         messages.error(self.request, _("You don't have the rights to change another user."))
    #         return redirect('users_list')
    #
    #     return render(request, 'users/user_delete.html')

    def form_valid(self, form):
        # try:
        #     user_delete = super(UserDeleteView, self).form_valid(form)
        messages.success(self.request, _('The user has been successfully deleted'))
        return super(UserDeleteView, self).form_valid(form)
        #     return user_delete
        # except ProtectedError:
        #     messages.error(self.request, _("It is not possible to delete a user because it is being usedss"))
        #     return redirect('users_list')
