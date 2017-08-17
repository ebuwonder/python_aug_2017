from django.shortcuts import render, HttpResponse, redirect

# def index(request):
#     response = 'woyonu!!'
#     return HttpResponse(response)

# Create your views here.
def index(request):
    context = {
        'email' : 'emmayah2@gmail.com',
        'name'  : 'ody'
    }
    return render(request, 'blogs/index.html', context)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
