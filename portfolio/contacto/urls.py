from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import crearContacto, AvisoContacto

urlpatterns = [
    path('crearcontacto/', crearContacto, name = 'crearcontacto'),
    path('avisocontacto/', AvisoContacto, name = 'avisocontacto')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)