"""from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import AntiSala, SalaCofre, SalaEnergia, SalaTelecom, RegistroGeral

@receiver(post_delete, sender=AntiSala)
def delete_registro_geral_for_antisala(sender, instance, **kwargs):

    #Deleta o registro correspondente em RegistroGeral quando uma AntiSala é deletada.


    RegistroGeral.objects.filter(
        tipo_sala='ANTISALA',
        data_criacao=instance.created_at.date()
    ).delete()

@receiver(post_delete, sender=SalaCofre)
def delete_registro_geral_for_salacofre(sender, instance, **kwargs):

    #Deleta o registro correspondente em RegistroGeral quando uma SalaCofre é deletada.

    RegistroGeral.objects.filter(
        tipo_sala='COFRE',
        data_criacao=instance.created_at.date()
    ).delete()

@receiver(post_delete, sender=SalaEnergia)
def delete_registro_geral_for_salaenergia(sender, instance, **kwargs):

    #Deleta o registro correspondente em RegistroGeral quando uma SalaEnergia é deletada.

    RegistroGeral.objects.filter(
        tipo_sala='ENERGIA',
        data_criacao=instance.created_at.date()
    ).delete()

@receiver(post_delete, sender=SalaTelecom)
def delete_registro_geral_for_salatelecom(sender, instance, **kwargs):

    #Deleta o registro correspondente em RegistroGeral quando uma SalaTelecom é deletada.

    RegistroGeral.objects.filter(
        tipo_sala='TELECOM',
        data_criacao=instance.created_at.date()
    ).delete()"""


from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import AntiSala, SalaCofre, SalaEnergia, SalaTelecom, RegistroGeral

# Lista com todas as subclasses de SalaBase
SALA_MODELS = [AntiSala, SalaCofre, SalaEnergia, SalaTelecom]

@receiver(post_delete)
def delete_registro_geral(sender, instance, **kwargs):
    """
    Deleta o registro correspondente em RegistroGeral quando qualquer sala é deletada.
    """
    # Verifica se o sender é uma das subclasses de SalaBase
    if sender in SALA_MODELS:
        tipo_sala_mapping = {
            AntiSala: 'ANTISALA',
            SalaCofre: 'COFRE',
            SalaEnergia: 'ENERGIA',
            SalaTelecom: 'TELECOM',
        }
        
        tipo_sala = tipo_sala_mapping.get(sender)
        if tipo_sala:
            RegistroGeral.objects.filter(
                tipo_sala=tipo_sala,
                data_criacao=instance.created_at.date()
            ).delete()

# Conecta o sinal às subclasses de SalaBase
for model in SALA_MODELS:
    post_delete.connect(delete_registro_geral, sender=model)
