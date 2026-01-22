from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Motorista, Gestor

class MotoristaInline(admin.StackedInline):
    model = Motorista
    can_delete = False
    verbose_name_plural = 'Perfil de Motorista'

class GestorInline(admin.StackedInline):
    model = Gestor
    can_delete = False
    verbose_name_plural = 'Perfil de Gestor'

class CustomUserAdmin(UserAdmin):
    inlines = (MotoristaInline, GestorInline)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Motorista)
admin.site.register(Gestor)