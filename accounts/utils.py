from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, message
from django.conf import settings

def detectRole(user):
	if user.role==1:
		redirect_role='VendorDash'
	elif user.role==2:
		redirect_role='CustomerDash'
	elif user.role==None and user.is_admin:
		redirect_role='/admin'
	return redirect_role


def send_email_token(request,user,subject,email_template):
	current_site=get_current_site(request)
	messages=render_to_string(email_template,{
		'domain':current_site,
		'user':user,
		'uid':urlsafe_base64_encode(force_bytes(user.pk)),
		'token':default_token_generator.make_token(user),
		})
	from_email=settings.EMAIL_HOST
	to_email=user.email
	mail=EmailMessage(subject,messages,from_email,to=[to_email])
	mail.send()