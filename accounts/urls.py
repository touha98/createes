from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name= 'login'),
    path('create', views.create, name= 'create'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    path('logout', views.logout, name='logout'),
    path('change_password', views.edit, name= 'edit'),
    path('reset', views.reset, name= 'reset'),
]