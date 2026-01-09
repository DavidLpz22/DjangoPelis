from django.shortcuts import render, redirect, get_object_or_404
from mainApp.models import Pelicula, Categoria, Participante
from .forms import PeliculaForm
# Create your views here.

def home(request):
    peliculas = Pelicula.objects.all()
    peliculas = Pelicula.objects.all().order_by('-id')

    categorias = Categoria.objects.all()
    participantes = Participante.objects.all()


    busqueda = request.GET.get('buscar')
    if busqueda:
        peliculas = peliculas.filter(titulo__icontains=busqueda)

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        peliculas = peliculas.filter(categoria_id=categoria_id)

    participante_id = request.GET.get('participante')
    if participante_id:
        peliculas = peliculas.filter(recomendado_por_id=participante_id)

    contexto = {
        'peliculas': peliculas,
        'categorias': categorias,
        'participantes': participantes,
        'busqueda_actual': busqueda, 
        'cat_actual': int(categoria_id) if categoria_id else None,
        'part_actual': int(participante_id) if participante_id else None,
    }
    return render(request, 'home.html', contexto)

def pelicula_detalle(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})

def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def participante_lista(request):
    participantes = Participante.objects.all()
    return render(request, 'lista_participantes.html', {'participantes': participantes})

def agregar_pelicula(request):
    if request.method == 'POST':

        formulario = PeliculaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = PeliculaForm()

    return render(request, 'agregar_pelicula.html', {'formulario': formulario})

def eliminar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    
    if request.method == 'POST':
        pelicula.delete()
        return redirect('home') 
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})