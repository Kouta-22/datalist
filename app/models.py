from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class RegistroGeral(models.Model):
    TIPO_SALA_CHOICES = [
        ('ANTISALA','Antisala'),
        ('COFRE','SalaCofre'),
        ('TELECOM','SalaTelecom'),
        ('ENERGIA','SalaEnergia')
    ]
    tipo_sala = models.CharField(max_length=10, choices=TIPO_SALA_CHOICES)
    observacao = models.CharField(max_length=250, null=True,blank=True)
    temperatura = models.DecimalField(max_digits=5,decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_sala} - {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"




# Classe Base para todas as salas
class SalaBase(models.Model):
    LIMPEZA_CHOICES = [
        ('L', 'Limpo'),         # 'L' representa "Limpo"
        ('M', 'Mais ou Menos'), # 'M' representa "Mais ou Menos"
        ('S', 'Sujo'),          # 'S' representa "Sujo"
    ]
 
    observation = models.CharField(max_length=250, null=True, blank=True)  # Observação opcional
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Exemplo: 23.45°C
    limpeza = models.CharField(  # Campo de limpeza com opções pré-definidas
        max_length=1,
        choices=LIMPEZA_CHOICES,
        default='L',  # Valor padrão: "Limpo"
    )

    class Meta:
        abstract = True  # Define que esta classe é abstrata e não será migrada

# Modelos específicos para cada sala
class AntiSala(SalaBase):
    def __str__(self):
        return "Antisala"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        RegistroGeral.objects.create(
            tipo_sala='ANTISALA',
            observacao=self.observation,
            temperatura = self.temperature,
            data_criacao=self.created_at.date()
        )

class SalaCofre(SalaBase):
    def __str__(self):
        return "SalaCofre"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        RegistroGeral.objects.create(
            tipo_sala='COFRE',
            observacao=self.observation,
            temperatura = self.temperature,
            data_criacao=self.created_at.date()
        )
    

class SalaTelecom(SalaBase):
    def __str__(self):
        return "SalaTelecom"

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        RegistroGeral.objects.create(
            tipo_sala='TELECOM',
            observacao=self.observation,
            temperatura = self.temperature,
            data_criacao=self.created_at.date()
        )
    

class SalaEnergia(SalaBase):
    def __str__(self):
        return "SalaEnergia"

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        RegistroGeral.objects.create(
            tipo_sala='ENERGIA',
            observacao=self.observation,
            temperatura = self.temperature,
            data_criacao=self.created_at.date()
        )