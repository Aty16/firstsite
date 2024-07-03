from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
from .forms import SignupForm, LoginForm, ContactForm


def  home(request):
    
    return render(request, 'gsite/index.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    
    else:
        form = LoginForm()
    return render(request, 'gsite/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = SignupForm()
    return render(request, 'gsite/signup.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('home')


def projects(request):
    return render(request, 'gsite/projects.html')


def services(request):
    return render(request, 'gsite/services.html')


def aboutus(request):
    return render(request, 'gsite/aboutus.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     "Subject here",
            #     "Here is the message.",
            #     "from@example.com",
            #     ["to@example.com"],
            #     fail_silently=False,
            # )
            form.save()
            return render(request, 'gsite/contsuccess.html')
    form = ContactForm()
    context = {'form': form}
    return render (request, 'gsite/contact.html', context)
