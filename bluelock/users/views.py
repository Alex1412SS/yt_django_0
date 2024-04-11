from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import New_user_form, profile
from django.contrib.auth import login, logout
from .models import profile_model


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


def profilee(request, username):
    if request.method == 'POST':
       user = request.user
       image = request.FILES['image']
       profile = profile_model(user=user, image=image)
       profile.save()
    return render(request, 'users/profile.html')

def seller_profile(request, id):
    seller = User.objects.get(id=id)
    context = {
        'seller': seller
    }
    return render(request, 'users/seller.html', context)