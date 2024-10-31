from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('<str:tipo_sala>/',views.registrar_sala,name='registrar_sala')
]
