from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agendar/', views.agendar, name='agendar'),
    path('servicos/', views.servicos, name='servicos'),
]