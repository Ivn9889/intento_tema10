from django.shortcuts import render

# Create your views here.
def saludo(request):
    contexto = {'mensaje': 'Hola Django - Coder'} 
    return render(request, 'miapp/saludo.html', contexto)
