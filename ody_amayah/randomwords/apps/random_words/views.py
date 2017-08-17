from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'random_words/index.html', context)

def generate(request):
    return redirect('/')
