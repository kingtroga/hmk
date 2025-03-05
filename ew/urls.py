from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LogInForm
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', LoginView.as_view(template_name='ew/login.html', authentication_form=LogInForm), name="login"),
    path('logout/', views.logout_view,  name='logout'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]