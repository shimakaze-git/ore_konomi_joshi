from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import RegisterForm

# Create your views here.
 
 
def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'user/index.html', context)
 
 
@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'user/profile.html', context)
 
 
def regist(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'user/regist.html', context)
 
 
@require_POST
def regist_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('auth:index')
 
    context = {
        'form': form,
    }
    return render(request, 'user/regist.html', context)
    