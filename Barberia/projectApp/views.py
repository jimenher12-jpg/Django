from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'inicio/home.html')

def about(request):
    return render(request, 'inicio/about.html')

def blog(request):
    return render(request, 'inicio/blog.html')

def contacto(request):
    return render(request, 'inicio/contacto.html') 
