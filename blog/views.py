from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Asegúrate de que exista un archivo `home.html` en la carpeta de templates
