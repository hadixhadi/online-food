from django.urls import path
from . views import UserRegister , VendorRegister
urlpatterns = [
    path('UserRegister/',UserRegister,name='UserRegister'),
    path('VendorRegister/',VendorRegister,name='VendorRegister')
]
