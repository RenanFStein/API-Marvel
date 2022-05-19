from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_view/', views.cadastro_view, name='cadastro_view'),    
    path('login/', views.login, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
]