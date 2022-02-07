from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper


class SubmitForm(forms.Form):
    text = forms.CharField(label='Text:', widget=forms.Textarea(attrs={'rows': 5, 'cols': 20, 'data-length': 2048}))
    box_size = forms.IntegerField(label='Box size:', min_value=1, max_value=50, initial=10)
    border = forms.IntegerField(label='Border size:', min_value=0, max_value=10, initial=5)
    back_color = forms.CharField(label='Background:', widget=forms.TextInput(attrs={'type': 'color'}),
                                 initial="#ffffff")
    fill_color = forms.CharField(label='Fill:', widget=forms.TextInput(attrs={'type': 'color'}),
                                 initial="#000000")


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
