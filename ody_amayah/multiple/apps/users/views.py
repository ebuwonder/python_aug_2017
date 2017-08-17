from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def register(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def login(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)
