from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import registrationform

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = registrationform()

    return render(request, 'register.html', {'form':form})

from .forms import customloginform

def custom_login(request):
    if request.method == 'POST':
        form = customloginform(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = customloginform()

    return render(request, 'login.html', {'form':form})

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'home.html')
