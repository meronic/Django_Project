from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'introduce'

urlpatterns = [
    
    path('', auth_views.LoginView.as_view(template_name='introduce/index.html')),
    
]