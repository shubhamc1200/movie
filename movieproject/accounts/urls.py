
from django.contrib import admin
from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('signIn/',views.signIn,name="signIn"),
    path('postsign/',views.postsign,name="postsign"),
    path('logout/',views.logout,name="log"),
    path('signup/',views.signUp,name="signUp"),
    path('postsignup/',views.postsignup,name="postsignup"),
]
