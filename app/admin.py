from django.contrib import admin
from .models import AntiSala, SalaCofre, SalaTelecom, SalaEnergia,RegistroGeral


@admin.register(AntiSala)
class Admin_AntiSala(admin.ModelAdmin):
    list_display = ('__str__','created_at')

@admin.register(SalaCofre)
class Admin_SalaCofre(admin.ModelAdmin):
    list_display = ('__str__','created_at')

@admin.register(SalaTelecom)
class Admin_SalaTelecom(admin.ModelAdmin):
    list_display = ('__str__','created_at')

@admin.register(SalaEnergia)
class Admin_SalaEnergia(admin.ModelAdmin):
    list_display= ('__str__','created_at')

@admin.register(RegistroGeral)
class Admin_Registro_Geral(admin.ModelAdmin):
    list_display=('tipo_sala','temperatura','data_criacao','observacao')
    list_filter = ('tipo_sala','data_criacao')
    search_fields = ('observacao',)