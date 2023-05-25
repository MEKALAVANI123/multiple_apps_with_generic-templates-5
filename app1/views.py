from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_string(request):
    return HttpResponse('This is app1_string')

def app1(request):
    return render(request,'app1.html')
