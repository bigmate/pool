from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateUserForm, LoginForm
from userprofile.models import MyUser
from django.utils.text import capfirst
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            print(form.is_valid())
            try:
                MyUser.objects.get(email=form.cleaned_data['email'])
                return render(request, 'signup/signup.html', {'form': form, 'msg': 'User exists'})
            except:
                MyUser.objects.create_user(
                    username=capfirst(form.cleaned_data['first_name'].lower()),
                    email=form.cleaned_data['email'],
                    first_name=capfirst(form.cleaned_data['first_name'].lower()),
                    password=form.cleaned_data['password'],
                    balance = 300
                )
                user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    auth_login(request, user)

        return HttpResponseRedirect(reverse('home:home', current_app='home'))
    form = CreateUserForm()
    return render(request, 'signup/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home:home',current_app='home'))
        form = LoginForm()
        return render(request, 'login/login.html',{'form':form,'msg':'username or password are invalid!'})
    form = LoginForm()
    return render(request, 'login/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:home',current_app='home'))