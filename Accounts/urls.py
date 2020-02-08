from django.urls import path
from .views import members, logout, login, profile, register

urlpatterns = [
    path('members/',members,name="members"),
    path('logout/',logout,name="logout"),
    path('login/',login,name="login"),
    path('profile/',profile,name="profile"),
    path('register/',register,name="register"),
]