from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.get_home_page, name='home'),
    path('', include('users.urls')),
    path('', include('statuses.urls')),
    path('', include('labels.urls')),
    path('', include('tasks.urls')),
    prefix_default_language=False
)
