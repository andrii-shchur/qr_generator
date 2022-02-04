from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('login/', views.sign_in_page, name='signin-page'),
    path('register/', views.register_page, name='register-page'),
]
