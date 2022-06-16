"""expenses URL Configuration

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
from django.urls import path, reverse_lazy
from receipts.views import show_receipts, show_accounts, show_expensecategory
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("receipts/", show_receipts, name="home"),
    # path("receipts/", show_accounts, name="arbitrary"),
    # path("receipts/", show_expensecategory, name="arbitrary"),
    path("", RedirectView.as_view(url=reverse_lazy("home"))),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
]
