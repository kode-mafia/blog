from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse('This is blog page')  
    context = {
       'data': 'This is blog page'
    }  
    return render(request, 'home.html', context)

def  blog(request):
    return HttpResponse('This is blog page')    
