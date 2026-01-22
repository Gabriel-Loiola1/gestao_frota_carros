from django.contrib import admin
from .models import Veiculo, Movimentacao

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa', 'km_atual', 'status_formatado')
    
    list_filter = ('status',)
    
    search_fields = ('modelo', 'placa')
    
    ordering = ('modelo',)

    @admin.display(description='Status')
    def status_formatado(self, obj):
        return obj.get_status_display()

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'motorista_nome', 'data_saida', 'km_saida', 'data_retorno', 'situacao')
    
    list_filter = ('data_saida', 'veiculo')
    
    search_fields = ('veiculo__placa', 'motorista__user__username', 'motorista__user__first_name')
    
    date_hierarchy = 'data_saida'

    @admin.display(description='Motorista')
    def motorista_nome(self, obj):
        return obj.motorista.user.username

    @admin.display(description='Situação')
    def situacao(self, obj):
        if obj.data_retorno:
            return "✅ Finalizada"
        return "🚗 Em Curso"