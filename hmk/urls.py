"""hmk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import index
from django.conf import settings
from django.conf.urls import handler403, handler404, handler500

urlpatterns = [
    path('atarysworld/', admin.site.urls),
    path('', index, name='index'),
    path('embracewellness/', include('hmk.ew.urls')),
    path('embracewellness/forum/', include('hmk.forum.urls')),
    path('embracewellness/blog/', include('hmk.blog.urls')),
    path('embracewellness/profile/', include('hmk.accounts.urls')),
    path('embracewellness/conversation/', include('hmk.conversation.urls')),
    path('embracewellness/direct_messages/', include('hmk.contact.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'hmk.ew.views.page_not_found'
handler403 = 'hmk.ew.views.permission_denied'
handler500 = 'hmk.ew.views.server_error'