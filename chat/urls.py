from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



app_name = 'message'
urlpatterns = [
    path('index', views.index, name = 'index'),
    # path('index/', views.index, name = 'index'),
    path('talk/<str:room_name>/', views.room, name='room'),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ajax', views.ajax, name = 'ajax'),
]
