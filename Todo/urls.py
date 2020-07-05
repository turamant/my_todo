from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('todo/', include('tasks.urls')),
]
