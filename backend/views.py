from django.shortcuts import render, redirect
from django.http import HttpResponse
from generator import make_code

from .forms import SubmitForm, SignInForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import QrCode

import uuid


def index(request):
    form = SubmitForm()
    return render(request, 'backend/index.html', {'form': form})


def submit(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            box_size = form.cleaned_data.get('box_size')
            border = form.cleaned_data.get('border')
            back_color = form.cleaned_data.get('back_color')
            fill_color = form.cleaned_data.get('fill_color')

            img_path = f'/static/img/{uuid.uuid4().hex}.png'
            make_code(text, box_size=box_size, border=border, back_color=back_color, fill_color=fill_color,
                      filename=img_path)

            return render(request, 'backend/result.html', {'img_path': img_path})


def login_page(request):
    form = SignInForm()

    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(index)

    return render(request, 'backend/signin-page.html', {'form': form})


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_page)

    return render(request, 'backend/register-page.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect(index)


def profile(request):
    query = QrCode.objects.filter(user=request.user)
    codes = []
    for el in query:
        codes.append(el.img_path)
    return render(request, 'backend/profile.html', {'codes': codes})


def save_code(request):
    new_code = QrCode(user=request.user, img_path=request.POST.get('img-path'))
    new_code.save()
    messages.success(request, 'Successfully saved!')
    return render(request, 'backend/result.html', {'img_path': request.POST.get('img-path')})

