from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Quiz

def qpage(request):
    questions = Quiz.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate and login user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('questions')  # Redirect to the questions page
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
