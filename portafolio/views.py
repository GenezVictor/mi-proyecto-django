from django.shortcuts import render
from .models import Proyecto

def pagina_inicio(request):
    proyectos = Proyecto.objects.filter(destacado=True)
    return render(request, 'portafolio/inicio.html', {
        'proyectos': proyectos
    })
