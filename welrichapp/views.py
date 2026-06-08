from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def art_to_cart(request):
    return render(request, 'cart.html')
