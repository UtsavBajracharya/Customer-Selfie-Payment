from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, LoginForm, EditForm, AppUserRegister
from .models import AppUser
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        app_form = AppUserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            appuser = app_form.save(commit=False)
            appuser.user = user
            appuser.save()
            username = form.cleaned_data.get('username') 
            login(request, user)
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('/home/1')
        else:
            messages.warning(request, f'Your password does not meet the criteria!')
    form = UserRegisterForm()
    app_form = AppUserRegister()
    return render(request, 'users/register.html', {'form': form, 'app_form': app_form})

def fyp_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are logged in as { username }!!')
            return redirect('/home/1')
        else:
            messages.warning(request, f'The username or password is incorrect!')
    else:
        return render(request, 'users/login.html', context={"form": form})

    form = LoginForm()
    return render(request, 'users/login.html', context={"form": form})


def fyp_logout(request):
    logout(request)
    return render(request, 'users/logout.html')
    return redirect('fyp:fyp-logout')


def profile(request):
    appuser = AppUser.objects.get(user=request.user)
    # detail = User.objects.get(pk=pk)
    # if detail.is_superuser:
    #     other = None
    # else:
    #     other = AppUser.objects.get(user_id=pk)
    context = {
        "appuser": appuser
        }
    return render(request, 'users/profile.html', context)


def add_funds(request):
    previous_funds = AppUser.objects.get(user=request.user).funds
    if request.method == "POST":
        funds = int(request.POST['fund'])
        funds = funds + previous_funds
        AppUser.objects.filter(user=request.user).update(funds=funds)
        return profile(request)
    return render(request, 'users/add_funds.html')  


def edit_profile(request, pk):
    if request.method == "POST":
        form = EditForm(data = request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('users:fyp-profile')
    else:
        form = EditForm(instance = request.user)
        context={
            "form": form
        }
        return render(request, 'users/edit_profile.html',context)


