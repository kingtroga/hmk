from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("professionals/", views.professionals, name='professionals'),
    path("<str:username>/", views.detail, name='detail'),
    path("edit/<int:pk>/", views.edit_profile_text, name='edit_profile_text'),
    path("edit/picture/", views.edit_profile_pic, name='edit_profile_pic'),
]