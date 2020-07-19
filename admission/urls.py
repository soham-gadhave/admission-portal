"""admission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from user_login_reg import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.main, name='home-page'),
    path('register/', user_views.register, name='register'),
    path('register/otp/', user_views.otp, name='verification'),
    path('v_register/', user_views.v_register),
    path('register/payment/', user_views.payment),
    path('login/', user_views.login, name='login'),
    path('login/applicant_login/', user_views.applicant_login, name='applicant-login'),
    path('login/verifier_login/', user_views.verifier_login, name='verifier-login'),
    # path('login/student_login/password_reset/', user_views.),
    # path('login/verifier_login/password_reset/', user_views.),
    path('applicant_home/', user_views.applicant_home, name='applicant-home'),
    path('applicant_home/display/', user_views.display, name='display'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_login_reg/logout.html'), name='logout'),
]
