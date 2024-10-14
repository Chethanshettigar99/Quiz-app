from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from quiz.models import Quiz

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Correctly call login with request and user
            return redirect('questions')  # Redirect to questions page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    


def questions(request):
    questions = Quiz.objects.all()
    return render(request, 'quiz.html', {'questions': questions})
