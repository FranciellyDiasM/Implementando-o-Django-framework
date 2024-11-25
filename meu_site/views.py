from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def brasil(request):
    return render(request, 'brasil.html')

def movimento(request):
    return render(request, 'movimento.html')

def origem(request):
    return render(request, 'origem.html')

def prevencao(request):
    return render(request, 'prevencao.html')