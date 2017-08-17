from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'session_words/index.html')

def add_word(request):
    print request.method
    return render(request, '/index.html')

def clear(request):
    return redirect('/')
