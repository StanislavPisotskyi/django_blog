"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from app import views as app_views
from users import views as user_views

urlpatterns = [
    re_path(r'^$', app_views.index, name='index_page'),
    re_path(r'^register$', user_views.register, name='register_page'),
    re_path(r'^login', user_views.sign_in, name='login_page'),
    re_path(r'^logout$', user_views.sign_out, name='logout_page'),
    path('admin/', admin.site.urls),
]