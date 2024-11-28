from django.shortcuts import render, redirect
from .models import AntiSala, SalaCofre, SalaEnergia, SalaTelecom,RegistroGeral
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.utils import DataError
from django.shortcuts import get_object_or_404, redirect
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
        image = request.FILES.get('image')
        
        # Bloco try para tratar erros de criação
        try:
            if tipo_sala == 'antisala':
                sala = AntiSala(observation=observation,temperature=temperature,limpeza=limpeza,image=image)
                tipo_sala_registro = 'ANTISALA'
            elif tipo_sala == 'salacofre':
                sala = SalaCofre(observation=observation,temperature=temperature,limpeza=limpeza,image=image)
                tipo_sala_registro = 'COFRE'
            elif tipo_sala == 'salaenergia':
                sala = SalaEnergia(observation=observation,temperature=temperature,limpeza=limpeza,image=image)
                tipo_sala_registro = 'ENERGIA'
            elif tipo_sala == 'salatelecom':
                sala = SalaTelecom(observation=observation,temperature=temperature,limpeza=limpeza,image=image)
                tipo_sala_registro = 'TELECOM'
            else:
                messages.error(request, "Tipo de sala inválido.")
                return redirect('home')
            sala.save(user=request.user)

            RegistroGeral.objects.update_or_create(
                tipo_sala=tipo_sala_registro,
                observacao = observation,
                temperatura=temperature,
                data_criacao=sala.created_at.date(),
                user=request.user

            )

        except DataError:
            messages.error(request, "O texto na observação é muito longo. Reduza o tamanho e tente novamente.")
            return redirect(request.path_info)

        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao salvar os dados: {e}")
            return redirect('home')
        
        # Confirmação de sucesso ao usuário
        messages.success(request, "Registro salvo com sucesso!")
        return redirect('home')
    
    template_name = f'app/{tipo_sala}.html'
    return render(request, template_name)

@login_required
def deletar_registro(request, registro_id):
    """
    Exclui um registro da tabela RegistroGeral e sincroniza com as tabelas associadas.
    """
    registro = get_object_or_404(RegistroGeral, id=registro_id)
    try:
        registro.delete()
        messages.success(request, "Registro excluído com sucesso!")
    except Exception as e:
        messages.error(request, f"Erro ao excluir o registro: {e}")
    return redirect('home')