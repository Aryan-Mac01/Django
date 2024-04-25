from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description
        )
    
        return redirect('/receipes/')

    queryset = Receipe.objects.all()
    context = {'receipes': queryset}

    return render(request, 'receipes.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        
        else:
            login(user)
            return redirect('/receipes')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username

        )

        user.set_password(password)
        user.save()

        return redirect('/register/')

    return render(request, 'register.html')

