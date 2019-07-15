from django.shortcuts import render, HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponseRedirect("/")

def number(request,num):
    return HttpResponse("Your number is:"+num)

def edit(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")

def delete(request,num): #you need to add num to argument!
    return HttpResponseRedirect("/")