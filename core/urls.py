# core\urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Lista as rotas do app "cadastro"
    path('', include('cadastro.urls')),
]
