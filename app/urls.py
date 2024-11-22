from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),  
    path('logout/', views.logout_view, name='logout'),
    path('<str:tipo_sala>/', views.registrar_sala, name='registrar_sala'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
