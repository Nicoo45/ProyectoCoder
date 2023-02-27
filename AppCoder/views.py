from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')    

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')
'''
def cursoFormulario(request):
    if request.method == 'POST':
        curso= Curso(request.POST['curso'], request.POST['comision'])
        curso.save()
        return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/cursoFormulario.html")
'''
def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], comision=informacion['comision'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})