from django.urls import path
from . views import UserRegister
urlpatterns = [
    path('UserRegister/',UserRegister,name='UserRegister')
]
