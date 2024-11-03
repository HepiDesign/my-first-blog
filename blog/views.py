from django.shortcuts import render

def post_list(request):
    return render(request, 'home.html')  # Asegúrate de que exista un archivo `home.html` en la carpeta de templates

