from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_string(request):
    return HttpResponse('This is app2_string')

def app2(request):
    return render(request,'app2.html')