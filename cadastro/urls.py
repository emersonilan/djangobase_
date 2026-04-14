# cadastro\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Rota para a página de contato
    path('contato/', views.contato, name='contato'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('pessoa/<int:id>/', views.detalhe, name='detalhe'),
    path('pessoa/<int:id>/editar/', views.editar, name='editar'),
    path('pessoa/<int:id>/deletar/', views.deletar, name='deletar'),
]