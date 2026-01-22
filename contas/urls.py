from django.urls import path
from . import views

urlpatterns = [
    path('novo-motorista/', views.cadastrar_motorista, name='cadastrar_motorista'),
    path('novo-gestor/', views.cadastrar_gestor, name='cadastrar_gestor'),
]
