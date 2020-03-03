from django.urls import path, include
from .api import Register, Login
from knox import views as knox_views

urlpatterns = [
    path('', include('knox.urls')),
    path('register', Register.as_view()),
    path('login', Login.as_view())
]
