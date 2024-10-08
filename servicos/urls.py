from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_servico, name="listar_servico"),
    path('novo_servico/', views.novo_servico, name="novo_servico"),
    path('listar_servico/', views.listar_servico, name="listar_servico"),
    path('servico/<int:id>/', views.servico, name="servico"),
    path('gerar_os/<int:id>/', views.gerar_os, name="gerar_os"),
]