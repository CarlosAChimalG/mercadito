from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='Authentication/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name='Authentication/logout.html'), name= 'logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('mainAdmin/', views.mainAdmin, name='mainAdmin'),
    path('seller/', views.seller, name='seller'),
    path('products/', list_products, name='products'),
    path('payments/', payments, name='payments'),
   
    
    path('prueba1/', views.prueba1, name='prueba1'),
    path('prueba2/', views.prueba2, name='prueba2'),
]
