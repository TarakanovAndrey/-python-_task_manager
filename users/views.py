from django.shortcuts import render, redirect
from . forms import RegisterUserForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users_list'


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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('users_list')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(UserUpdateView, self).handle_no_permission()

    def get(self, request, *args, **kwargs):

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


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_list')
    success_message = _('The user has been successfully deleted')

    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return super(UserDeleteView, self).handle_no_permission()

    def form_valid(self, form):
        if self.object != self.request.user:
            messages.error(self.request, _("You don't have the rights to change another user."))
            return redirect('users_list')

        try:
            return super(UserDeleteView, self).form_valid(form)
        except ProtectedError:
            messages.error(self.request, _("It is not possible to"
                                           " delete a user because it is being usedss"))
            return redirect('users_list')
