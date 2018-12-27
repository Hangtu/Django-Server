from django.http import HttpResponse

def home(req):
    return HttpResponse('homepage')

def about(req):
    return HttpResponse('about')