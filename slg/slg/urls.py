from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('clientes/', include('cliente.urls')),
    path('citas/', include('cal.urls')),
]
