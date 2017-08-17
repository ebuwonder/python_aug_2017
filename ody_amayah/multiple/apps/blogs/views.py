from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def create(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def new(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response, 'blogs/new.html')

def show(request, blog_id):
  print blog_id
  return HttpResponse(response, 'blogs/show.html')

def edit(request, blog_id):
  response = "Hello, I am your first request!"
  return HttpResponse(response, 'blogs/show.html')

# def delete(request, blog_id)
#   return redirect('/blogs')


def route_param(request, blog_id):
    print blog_id
    return redirect('/')
