from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Motorista, Gestor

class UsuarioForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Usuário (Login)'
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['email'].label = 'E-mail'
        
        self.fields['password1'].label = 'Senha'
        self.fields['password1'].help_text = "A senha deve conter pelo menos 8 caracteres."
        self.fields['password2'].label = 'Confirmar Senha'

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['cnh', 'categoria_cnh', 'validade_cnh']
        widgets = {'validade_cnh': forms.DateInput(attrs={'type': 'date'})}

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['departamento', 'telefone']