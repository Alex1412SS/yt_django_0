from django.shortcuts import render, redirect
from .forms import New_user_form
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = New_user_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:baze')
    form = New_user_form
    context = {'form': form}
    return render(request, 'users/register.html', context)


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})


def profile(request, username):
    return render(request, 'users/profile.html')