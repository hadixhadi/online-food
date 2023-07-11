from django.urls import path
from . views import UserRegister , VendorRegister , login , myAccount, logout , VendorDash , CustomerDash
urlpatterns = [
    path('UserRegister/',UserRegister,name='UserRegister'),
    path('VendorRegister/',VendorRegister,name='VendorRegister'),
    path('login/',login,name='login'),
    path('myAccount/',myAccount,name='myAccount'),
    path('logout/',logout,name='logout'),
    path('VendorDash/',VendorDash,name='VendorDash'),
    path('CustomerDash/',CustomerDash,name='CustomerDash')
]
