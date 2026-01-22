from django import forms
from .models import Movimentacao, Veiculo

class FormVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'placa', 'km_atual', 'status']

class FormSaida(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['veiculo', 'observacao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.filter(status='disponivel')

class FormDevolucao(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['km_retorno', 'observacao']

    def clean_km_retorno(self):
        km = self.cleaned_data.get('km_retorno')
        km_saida = self.instance.km_saida
        if km and km < km_saida:
            raise forms.ValidationError(f'Erro: KM Atual ({km}) menor que KM Saída ({km_saida}).')
        return km