from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from . import views
from users.views import LoginUserView, LogoutUserView


urlpatterns = i18n_patterns(path('admin/', admin.site.urls),
                            path('i18n/', include('django.conf.urls.i18n')),
                            path('', views.get_home_page, name='home'),
                            path('users/', include('users.urls')),
                            path('statuses/', include('statuses.urls')),
                            path('labels/', include('labels.urls')),
                            path('tasks/', include('tasks.urls')),
                            path('login/', LoginUserView.as_view(), name='login'),
                            path('logout/', LogoutUserView.as_view(), name='logout'),
                            prefix_default_language=False,
                            )
