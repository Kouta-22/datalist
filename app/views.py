from django.shortcuts import render, redirect
from .models import AntiSala, SalaCofre, SalaEnergia, SalaTelecom
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Adiciona mensagem de erro ao framework de mensagens
            messages.error(request, 'Credenciais inválidas. Verifique seu login.')
            return redirect('login')
    
    return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    # Redireciona para login após o logout, com o parâmetro `next` para evitar vazamento de URL
    return redirect('login')

@login_required
def home(request):
    return render(request, 'app/home.html')

@login_required
def registrar_sala(request, tipo_sala):
    if request.method == 'POST':
        observation = request.POST.get('observation')
        temperature = request.POST.get('temperature')
        limpeza = request.POST.get('limpeza')
        
        # Bloco try para tratar erros de criação
        try:
            if tipo_sala == 'antisala':
                AntiSala.objects.create(observation=observation, temperature=temperature, limpeza=limpeza)
            elif tipo_sala == 'salacofre':
                SalaCofre.objects.create(observation=observation, temperature=temperature, limpeza=limpeza)
            elif tipo_sala == 'salaenergia':
                SalaEnergia.objects.create(observation=observation, temperature=temperature, limpeza=limpeza)
            elif tipo_sala == 'salatelecom':
                SalaTelecom.objects.create(observation=observation, temperature=temperature, limpeza=limpeza)
            else:
                messages.error(request, "Tipo de sala inválido.")
                return redirect('home')

        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao salvar os dados: {e}")
            return redirect('home')
        
        # Confirmação de sucesso ao usuário
        messages.success(request, "Registro salvo com sucesso!")
        return redirect('home')
    
    template_name = f'app/{tipo_sala}.html'
    return render(request, template_name)
