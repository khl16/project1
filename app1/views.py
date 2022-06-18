# from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def index2(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def intr(request,val):
    return HttpResponse(val)
# Create your views here.


# from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")
