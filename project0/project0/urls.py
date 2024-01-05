"""
URL configuration for project0 project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.profile, name='dashboard'),
    path('accounts/login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('create_item/', views.create_item, name='create_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('user_items/', views.user_items, name='user_items'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('all_items/', views.all_items, name='all_items'),
    # path('search/', views.search_items, name='search_items'),
    # path('category/<str:category>/', views.category_items, name='category_items'),
   
]
