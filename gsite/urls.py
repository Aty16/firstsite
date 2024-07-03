from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('projekte/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('ueberuns/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
]
