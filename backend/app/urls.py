"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
import django_cas_ng.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('src.urls')),
    path('cas/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),  # 访问cas服务的登录
    path('cas/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),  # 访问cas服务的登出
]