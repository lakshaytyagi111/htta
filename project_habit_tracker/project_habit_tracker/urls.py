"""
URL configuration for project_habit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allfunctions/', views.all_functions, name='allfunctions'),
    path('', views.all_functions, name='allfunctions'),
    path('save_habit_click', views.save_habit_click, name = 'save_habit_click'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/login/', views.login, name='login'),

]
