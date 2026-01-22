from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', core_views.dashboard, name='dashboard'),
    path('veiculo/novo/', core_views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('veiculo/editar/<int:id>/', core_views.editar_veiculo, name='editar_veiculo'),
    path('saida/', core_views.registrar_saida, name='registrar_saida'),
    path('devolucao/<int:id>/', core_views.registrar_devolucao, name='registrar_devolucao'),
    path('contas/', include('contas.urls')),
]
