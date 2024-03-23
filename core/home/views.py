from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
        {'name': 'Abhishek', 'age': 26},
        {'name': 'Aryan', 'age': 23},
        {'name': 'Ashutosh', 'age': 21},
        {'name': 'Pragati', 'age': 17}

    ] 

    

    vegetables = ['Pumpkin', 'Tomato', 'Potato']
    
    

    return render(request, "home/index.html", context = {'peoples' : peoples, 'vegetables' : vegetables })

def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")