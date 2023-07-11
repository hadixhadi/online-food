from django.shortcuts import render ,redirect
from .forms import UserRegisterFrom
from .models import User , UserProfile
from django.contrib import messages , auth
from Vendor.forms import VendorRegisterForm
from .utils import detectRole
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
#check role of vendor:
def vendor_role_checker(user):
    if user.role==1:
        return True
    else:
        return PermissionDenied

#check role of Customer
def Customer_role_checker(user):
    if user.role==2:
        return True
    else:
        return PermissionDenied



def UserRegister(request):
    if request.user.is_authenticated:
        messages.success(request,'you are loggedin !')
    elif request.method=='POST':
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
    if request.user.is_authenticated:
        messages.success(request,'you are loggedin !')
    elif request.method=='POST':

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


def login(request):
    if request.user.is_authenticated:
        messages.success(request,'you are loggedin !')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are loged in succsefully!')
            return redirect('myAccount')
        else:
            messages.error(request,'login field!')
            return redirect('login')

    return render(request,'accounts/login.html')
        
@login_required(login_url='login')
def myAccount(request):
    url=detectRole(request.user)
    return redirect(url)


@login_required(login_url='login')
def CustomerDash(request):
    if request.user.role==2:
        return render(request,'accounts/CustomerDash.html')
    else:
        raise PermissionDenied


@login_required(login_url='login')
def VendorDash(request):
    if request.user.role==1:
        return render(request,'accounts/VendorDash.html')
    else:
        raise PermissionDenied
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')