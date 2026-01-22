from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Veiculo, Movimentacao
from .forms import FormVeiculo, FormSaida, FormDevolucao
from contas.models import Motorista

@login_required
def dashboard(request):
    veiculos = Veiculo.objects.all()
    mov_abertas = Movimentacao.objects.filter(data_retorno__isnull=True)

    lista_motoristas = []
    if request.user.is_gestor:
        lista_motoristas = Motorista.objects.all()

    return render(request, 'dashboard.html', {
        'veiculos': veiculos, 'movimentacoes_abertas': mov_abertas, 'lista_motoristas': lista_motoristas
    })

@login_required
def cadastrar_veiculo(request):
    if not request.user.is_gestor:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FormVeiculo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado!')
            return redirect('dashboard')
    else:
        form = FormVeiculo()
    return render(request, 'form.html', {
        'form': form, 'titulo': 'Novo Veículo'
    })

@login_required
def editar_veiculo(request, id):
    if not request.user.is_gestor:
        return redirect('dashboard')
    veiculo = get_object_or_404(Veiculo, id=id)

    if request.method == 'POST':
        form = FormVeiculo(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FormVeiculo(instance=veiculo)
    return render(request, 'form.html', {
        'form': form, 'titulo': f'Editar {veiculo.modelo}'
    })

@login_required
def registrar_saida(request):
    if not request.user.is_motorista:
        messages.error(request, 'Acesso restrito a motoristas.')
        return redirect('dashboard')

    if request.method == 'POST':
        form = FormSaida(request.POST)
        if form.is_valid():
            mov = form.save(commit=False)
            mov.motorista = request.user.motorista
            mov.km_saida = mov.veiculo.km_atual
            mov.save()

            v = mov.veiculo
            v.status = 'em_uso'
            v.save()
            return redirect('dashboard')
    else:
        form = FormSaida()
    return render(request, 'form.html', {
        'form': form, 'titulo': 'Retirar Veículo'
    })

@login_required
def registrar_devolucao(request, id):
    mov = get_object_or_404(Movimentacao, id=id)
    if request.method == 'POST':
        form = FormDevolucao(request.POST, instance=mov)
        if form.is_valid():
            mov = form.save(commit=False)
            mov.data_retorno = timezone.now()
            mov.save()

            v = mov.veiculo
            v.status = 'disponivel'
            v.km_atual = mov.km_retorno
            v.save()
            messages.success(request, "Devolução realizada com sucesso!")
            return redirect('dashboard')
    else:
        form = FormDevolucao(instance=mov)
    return render(request, 'form.html', {
        'form': form, 'titulo': 'Devolver Veículo'
    })