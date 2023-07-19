from django.urls import path , include
from Vendor import urls
from . views import UserRegister , VendorRegister , login , myAccount, logout , VendorDash , CustomerDash , active,forget_password , reset_password_validate,reset_password
urlpatterns = [
    path('',myAccount),
    path('UserRegister/',UserRegister,name='UserRegister'),
    path('VendorRegister/',VendorRegister,name='VendorRegister'),
    path('login/',login,name='login'),
    path('myAccount/',myAccount,name='myAccount'),
    path('logout/',logout,name='logout'),
    path('VendorDash/',VendorDash,name='VendorDash'),
    path('CustomerDash/',CustomerDash,name='CustomerDash'),
    path('active/<uidb64>/<token>/',active,name='active'),
    path('forget_password/',forget_password,name='forget_password'),
    path('reset_password_validate/<uidb64>/<token>',reset_password_validate,name='reset_password_validate'),
    path('reset_password/',reset_password,name='reset_password'),
    path('vendor/',include('Vendor.urls')),
]
