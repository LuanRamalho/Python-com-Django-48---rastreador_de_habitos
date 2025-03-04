from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Habito, Registro
from datetime import datetime

def criar_habito(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        data_inicial = datetime.strptime(request.POST['data_inicial'], '%d/%m/%Y').date()
        data_final = datetime.strptime(request.POST['data_final'], '%d/%m/%Y').date()

        Habito.objects.create(nome=nome, descricao=descricao, data_inicial=data_inicial, data_final=data_final)
        return redirect('habitos/listar_habitos')

    return render(request, 'habitos/criar_habito.html')

def listar_habitos(request):
    habitos = Habito.objects.all()
    return render(request, 'habitos/listar_habitos.html', {'habitos': habitos})

def registrar_habito(request, habito_id):
    habito = Habito.objects.get(id=habito_id)
    if request.method == 'POST':
        data = datetime.strptime(request.POST['data'], '%d/%m/%Y').date()
        cumprido = 'cumprido' in request.POST
        Registro.objects.create(habito=habito, data=data, cumprido=cumprido)
        return redirect('habitos/relatorio_habito', habito_id=habito.id)

    return render(request, 'habitos/registrar_habito.html', {'habito': habito})

def relatorio_habito(request, habito_id):
    habito = Habito.objects.get(id=habito_id)
    registros = Registro.objects.filter(habito=habito)
    
    total_dias = (habito.data_final - habito.data_inicial).days + 1
    dias_cumpridos = registros.filter(cumprido=True).count()
    porcentagem = (dias_cumpridos / total_dias) * 100

    return render(request, 'habitos/relatorio_habito.html', {
        'habito': habito,
        'total_dias': total_dias,
        'dias_cumpridos': dias_cumpridos,
        'porcentagem': porcentagem,
        'registros': registros
    })
