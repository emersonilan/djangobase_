# cadastro\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Rota para a página de contato
    path('contato/', views.contato, name='contato'),
    path('adicionar/', views.adicionar, name='adicionar'),
]