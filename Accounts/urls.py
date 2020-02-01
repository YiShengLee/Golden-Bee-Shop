from django.urls import path
from .views import members, logout

urlpatterns = [
    path('members/',members,name="members"),
    path('logout/',logout,name="logout"),
]