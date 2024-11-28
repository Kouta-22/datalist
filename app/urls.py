from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import deletar_registro
urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),  
    path('logout/', views.logout_view, name='logout'),
    path('<str:tipo_sala>/', views.registrar_sala, name='registrar_sala'),
    path('deletar/<int:registro_id>/', deletar_registro, name='deletar_registro')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
