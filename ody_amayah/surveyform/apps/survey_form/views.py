from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def result(request):
    return render(request, 'survey_form/result.html')

def process(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    print request.method
    print request.POST['name']
    print request.POST['language']
    print request.POST['location']
    print request.POST['comment']
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    request.session['tries'] += 1
    return redirect('/result')
