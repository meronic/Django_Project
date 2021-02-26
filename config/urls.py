from django.contrib import admin
from django.urls import path, include
from pybo import views
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    
    path('main/', include('main.urls') ),

]
