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

    text = ""
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    

    return render(request, "home/index.html", context = {'peoples' : peoples, 'text' :text })

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")