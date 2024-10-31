from django.shortcuts import render, redirect
from .models import AntiSala,SalaCofre,SalaEnergia,SalaTelecom

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def registrar_sala(request,tipo_sala):
    if request.method == 'POST':
        observation = request.POST.get('observation')
        temperature = request.POST.get('temperature')
        limpeza = request.POST.get('limpeza')
        if tipo_sala == 'antisala':
            AntiSala.objects.create(
                observation=observation,
                temperature=temperature,
                limpeza=limpeza
            )
        elif tipo_sala == 'salacofre':
            SalaCofre.objects.create(
                observation=observation,
                temperature=temperature,
                limpeza=limpeza
            )
        elif tipo_sala == 'salaenergia':
            SalaEnergia.objects.create(
                observation=observation,
                temperature=temperature,
                limpeza=limpeza
            )
        elif tipo_sala == 'salatelecom':
            SalaTelecom.objects.create(
                observation = observation,
                temperature = temperature,
                limpeza = limpeza
            )
        else:
            return redirect('home')
        
        return redirect ('home')
    

    template_name = f'app/{tipo_sala}.html'
    return render (request,template_name)
