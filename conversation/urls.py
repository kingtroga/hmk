from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('<int:user_pk>/', views.detail, name='detail'),
    path('new/<int:user_pk>/', views.new_conversation, name='new'),
    path('', views.inbox, name='inbox'),
]