from django.contrib import admin
from .models import AntiSala, SalaCofre, SalaTelecom, SalaEnergia, RegistroGeral

# Configuração para AntiSala
@admin.register(AntiSala)
class Admin_AntiSala(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    list_filter = ('created_at',)  # Filtro por data de criação
    search_fields = ('observation',)  # Busca nas observações


# Configuração para SalaCofre
@admin.register(SalaCofre)
class Admin_SalaCofre(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('observation',)


# Configuração para SalaTelecom
@admin.register(SalaTelecom)
class Admin_SalaTelecom(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('observation',)


# Configuração para SalaEnergia
@admin.register(SalaEnergia)
class Admin_SalaEnergia(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('observation',)


# Configuração para RegistroGeral
@admin.register(RegistroGeral)
class Admin_Registro_Geral(admin.ModelAdmin):
    list_display = ('tipo_sala', 'temperatura', 'data_criacao', 'observacao', 'user')  # 'user' apenas no RegistroGeral
    list_filter = ('tipo_sala', 'data_criacao', 'user')  # Inclui filtro por usuário
    search_fields = ('observacao', 'user__username')  # Busca por observação e nome de usuário
    ordering = ('-data_criacao',)  # Ordena por data de criação decrescente
    list_per_page = 20  # Limita o número de registros por página no Admin
