from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('login/', views.login_page, name='login-page'),
    path('register/', views.register, name='register-page'),
    path('logout/', views.logout_page, name='logout-page'),
    path('profile/', views.profile, name='profile-page'),
    path('save-code/', views.save_code, name='save-code')
]
