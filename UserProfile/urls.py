"""
URL configuration for UserProfile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from user.views import (
    change_password_view,
    dashboard_view,
    forgot_password_view,
    login_view,
    logout_view,
    password_reset_confirm_view,
    profile_view,
    signup_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("forgot_password/", forgot_password_view, name="forgot_password"),
    path(
        "reset/<uid>/<token>/",
        password_reset_confirm_view,
        name="password_reset_confirm",
    ),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("profile/", profile_view, name="profile"),
    path("change_password/", change_password_view, name="change_password"),
    path("logout/", logout_view, name="logout"),
]
