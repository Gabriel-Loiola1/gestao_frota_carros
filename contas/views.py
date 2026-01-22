from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import UsuarioForm, MotoristaForm, GestorForm

@login_required
def cadastrar_motorista(request):
    if not request.user.is_gestor:
        messages.error(request, "Apenas gestores podem realizar cadastros.")
        return redirect('dashboard')

    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        profile_form = MotoristaForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                new_user = user_form.save()
                motorista = profile_form.save(commit=False)
                motorista.user = new_user
                motorista.save()
            messages.success(request, f'Motorista {new_user.username} criado!')
            return redirect('dashboard')
    else:
        user_form = UsuarioForm()
        profile_form = MotoristaForm()
    return render(request, 'registration/register_generic.html', {
        'user_form': user_form, 'profile_form': profile_form, 'titulo': 'Novo Motorista'
    })

@login_required
def cadastrar_gestor(request):
    if not request.user.is_gestor:
        return redirect('dashboard')
    
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        profile_form = GestorForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                new_user = user_form.save()
                gestor = profile_form.save(commit=False)
                gestor.user = new_user
                gestor.save()
            messages.success(request, f'Gestor {new_user.username} criado!')
            return redirect('dashboard')
    else:
        user_form = UsuarioForm()
        profile_form = GestorForm()
    return render(request, 'registration/register_generic.html', {
        'user_form': user_form, 'profile_form': profile_form, 'titulo': 'Novo Gestor'
    })