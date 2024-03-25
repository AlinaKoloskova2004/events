from django.urls import path
from . import views


app_name = 'register_author'

urlpatterns = [
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('account_confirm/', views.account_confirm, name='account_confirm'),
]