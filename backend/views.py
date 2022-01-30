from django.shortcuts import render
from django.http import HttpResponse
from generator import make_code

from .forms import SubmitForm, SignInForm, RegisterForm
from django.contrib.auth.models import User


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

            make_code(text, box_size=box_size, border=border, back_color=back_color, fill_color=fill_color)

            return render(request, 'backend/result.html')


def sign_in_page(request):
    form = SignInForm()
    return render(request, 'backend/signin-page.html', {'form': form})


def register_page(request):
    form = RegisterForm()
    return render(request, 'backend/register-page.html', {'form': form})


def sign_in(request):
    user = User.objects.create_user()
