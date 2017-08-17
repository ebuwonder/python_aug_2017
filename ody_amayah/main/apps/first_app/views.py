from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
    response = 'Hello, I am test'
    return HttpResponse(response)

def create(request):
    response = 'Hello, I am test'
    return HttpResponse(response)

def route_param(request, blog_id):
    print blog_id
    return redirect('/')
