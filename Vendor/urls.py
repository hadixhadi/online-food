from django.urls import path
from accounts import views as AccountViews
from .views import *
urlpatterns=[
	path('',AccountViews.VendorDash),
	path('profile/',profile,name='profile'),
]