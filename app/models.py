from django.db import models
from django.contrib.auth.models import User


# Modelo para RegistroGeral
class RegistroGeral(models.Model):
    TIPO_SALA_CHOICES = [
        ('ANTISALA', 'Antisala'),
        ('COFRE', 'SalaCofre'),
        ('TELECOM', 'SalaTelecom'),
        ('ENERGIA', 'SalaEnergia'),
    ]
    tipo_sala = models.CharField(max_length=10, choices=TIPO_SALA_CHOICES)
    observacao = models.CharField(max_length=250, null=True, blank=True)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_sala} - {self.data_criacao.strftime('%d/%m/%Y')}"

    def delete(self, *args, **kwargs):
        """
        Override do método delete para sincronizar exclusão com as tabelas de salas.
        """
        if self.tipo_sala == 'ANTISALA':
            AntiSala.objects.filter(created_at__date=self.data_criacao).delete()
        elif self.tipo_sala == 'COFRE':
            SalaCofre.objects.filter(created_at__date=self.data_criacao).delete()
        elif self.tipo_sala == 'TELECOM':
            SalaTelecom.objects.filter(created_at__date=self.data_criacao).delete()
        elif self.tipo_sala == 'ENERGIA':
            SalaEnergia.objects.filter(created_at__date=self.data_criacao).delete()
        super().delete(*args, **kwargs)


# Classe Base para salas
class SalaBase(models.Model):
    LIMPEZA_CHOICES = [
        ('L', 'Limpo'),
        ('M', 'Mais ou Menos'),
        ('S', 'Sujo'),
    ]
    observation = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    limpeza = models.CharField(
        max_length=1,
        choices=LIMPEZA_CHOICES,
        default='L',
    )
    image = models.ImageField(upload_to='uploads/salas/', null=True, blank=True)

    TIPO_SALA = None

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Override do método save para criar ou atualizar os registros na tabela mestre RegistroGeral.
        """
        user = kwargs.pop('user', None)
        super().save(*args, **kwargs)

        if self.TIPO_SALA:
            RegistroGeral.objects.update_or_create(
                tipo_sala=self.TIPO_SALA,
                data_criacao=self.created_at.date(),
                defaults={
                    'observacao': self.observation,
                    'temperatura': self.temperature,
                    'user': user,
                }
            )


# Modelos específicos para cada sala
class AntiSala(SalaBase):
    TIPO_SALA = 'ANTISALA'

    def __str__(self):
        return "Antisala"


class SalaCofre(SalaBase):
    TIPO_SALA = 'COFRE'

    def __str__(self):
        return "SalaCofre"


class SalaTelecom(SalaBase):
    TIPO_SALA = 'TELECOM'

    def __str__(self):
        return "SalaTelecom"


class SalaEnergia(SalaBase):
    TIPO_SALA = 'ENERGIA'

    def __str__(self):
        return "SalaEnergia"
