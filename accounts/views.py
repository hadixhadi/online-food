from django.shortcuts import render
from .forms import UserRegisterFrom
from .models import User , UserProfile
from django.contrib import messages
from Vendor.forms import VendorRegisterForm
# Create your views here.
def UserRegister(request):
    if request.method=='POST':
        form=UserRegisterFrom(request.POST)
        if form.is_valid():
            # user=form.save(commit=False)
            # user.role=User.CUSTOMER
            # user.save()
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,
                                          username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            messages.success(request,'account register succsefully!')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form=UserRegisterFrom()
    context={
        'form':form
    }
    return render(request,'accounts/userRegister.html',context)


def VendorRegister(request):
    if request.method=='POST':

        form=UserRegisterFrom(request.POST)
        v_form=VendorRegisterForm(request.POST,request.FILES)

        if form.is_valid() and v_form.is_valid:
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,
                                          username=username,email=email,password=password)
            user.role=User.VENDOR
            user.save()
            vendor=v_form.save(commit=False)
            vendor.user=user
            user_profile=UserProfile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()
            messages.success(request,'vendor registerd succsefully!')

    else:
        form=UserRegisterFrom()
        v_form=VendorRegisterForm()
    
    context={
        'form':form,
        'v_form':VendorRegisterForm,
    }
    return render(request,'accounts/VendorRegister.html',context)