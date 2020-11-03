from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm, TokenForm
from rest_framework.authtoken.models import Token


def register(request):
    title = 'Register'
    form = UserRegisterForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        form.save()
        messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('login')
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user or None)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile or None)
    token = Token.objects.get(user=request.user)
    t_form = TokenForm(instance=token or None)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'Your account has been updated')
        return redirect('profile')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        't_form': t_form,
    }
    return render(request, 'users/profile.html', context)
