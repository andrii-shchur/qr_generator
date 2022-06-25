from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import QrCode
from .forms import SubmitForm, SignInForm, RegisterForm
from generator import make_code

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
            return render(request, 'backend/result.html', {'img_path': img_path, 'created_at': str(timezone.now())})

        messages.add_message(request, messages.ERROR, 'Invalid input!')
        return redirect(index)

    else:
        messages.add_message(request, messages.ERROR, 'Error!')
        return redirect(index)


def login_page(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'You have already logged in!')
        return redirect(index)

    form = SignInForm()

    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                messages.add_message(request, messages.INFO, f"You are now logged in as {username}.")
                return redirect(index)

    elif request.method == 'GET':
        if request.GET.get('next') in ['/profile/', '/save-code/']:
            messages.add_message(request, messages.WARNING, 'You must log in first.')

    return render(request, 'backend/signin-page.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'You can\'t create accounts while logged in!')
        return redirect(index)

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_page)

    return render(request, 'backend/register-page.html', {'form': form})


def logout_page(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'bruh wtf')
        return redirect(index)

    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out.')
    return redirect(index)


@login_required
def profile(request):
    query = QrCode.objects.filter(user=request.user)
    data = []
    for el in query:
        data.append((el.img_path, el.created_at, el.img_path))
    return render(request, 'backend/profile.html', {'data': reversed(data)})


@login_required
def save_code(request):
    img_path = request.POST.get('img-path')
    created_at = request.POST.get('created-at')
    new_code = QrCode(user=request.user, img_path=img_path, created_at=created_at)
    new_code.save()
    messages.add_message(request, messages.SUCCESS, 'Successfully saved!')
    return redirect(index)
