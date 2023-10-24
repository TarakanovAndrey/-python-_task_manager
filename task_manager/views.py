from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def get_home_page(request):
    return render(
        request,
        template_name='task_manager/index.html',
        context={'logout_menu': {'users': _('Users'),
                                 'login': _('Login'),
                                 'registration': _('Registration')}}
    )
