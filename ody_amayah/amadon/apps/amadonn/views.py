from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'amadonn/index.html')

def checkout(request):
    return render(request, 'amadonn/checkout.html')

def buy(request):
    return redirect('/checkout.html')
