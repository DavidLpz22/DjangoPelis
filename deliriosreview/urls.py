from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pelicula/<int:pelicula_id>/', views.pelicula_detalle, name='pelicula_detalle'),
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('eliminar/<int:pelicula_id>/', views.eliminar_pelicula, name='eliminar_pelicula'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)