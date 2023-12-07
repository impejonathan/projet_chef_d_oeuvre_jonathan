# authentication/views.py
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from Livre_date import forms

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'Livre_date/index.html', {'first_name': request.user.first_name})
    else:
        return redirect('login')

    
def logout_user(request):
    
    logout(request)
    return redirect('login')



def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')  # change 'home' to 'index'
        message = 'Identifiants invalides.'
    return render(request, 'Livre_date/login.html', context={'form': form, 'message': message})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # change settings.LOGIN_REDIRECT_URL to 'index'
    return render(request, 'Livre_date/signup.html', context={'form': form})