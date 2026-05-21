from django.shortcuts import render, redirect, get_object_or_404
from.models import Tarea
# Create your views here.


#consultar listas tareas
def listar_tareas(request):
    tareas=Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas':tareas})

#Crear tarea
def crear_tarea(request):
    if request.method == "POST":
        titulo=request.POST['titulo']
        descripcion=request.POST['descripcion']
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('lista')
    return render(request, 'tareas/crear.html')

#Editar la tarea

def editar_tarea(request, id):
    tarea=get_object_or_404(Tarea,id=id)
    if request.method == 'POST':
        tarea.titulo=request.POST['titulo']
        tarea.descripcion=request.POST['descripcion']
        tarea.estado='estado' in request.POST
        tarea.save()
        return redirect('lista')
    return render(request, 'tareas/editar.html', {'tarea':tarea})

#eliminar tarea

def eliminar_tarea(request,id):
    tarea=get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('lista')

#filtro de tareas completadas
def completadas(request):
    tareas=Tarea.objects.filter(estado=True)
    return render(request, 'tareas/lista.html',{'tareas':tareas})