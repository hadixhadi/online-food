from django.db import models
from accounts.models import User , UserProfile
from accounts.utils import send_approval_email
# Create your models here.

class Vendor(models.Model):
	user=models.OneToOneField(User,related_name='user',
	on_delete=models.CASCADE)
	user_profile=models.OneToOneField(UserProfile,related_name='UserProfile',
	on_delete=models.CASCADE)
	vendor_name = models.CharField(max_length=50)
	vendor_license=models.ImageField(upload_to='vendor/license')
	is_approved=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	modified_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.vendor_name
	
	def save(self,*args,**kwargs):
		if self.pk is not None:
			orginal_approval=Vendor.objects.get(pk=self.pk)
			context={
				'user':self.user,
				'to_email':self.user.email,
				'is_approved':self.is_approved
			}
			if orginal_approval.is_approved != self.is_approved:
				if self.is_approved==True:
					subject="your resturant has been approved!"
					template='accounts/email/approval.html'
					send_approval_email(subject,template,context)
				else:
					subject="your resturant does not approved!"
					template='accounts/email/approval.html'
					send_approval_email(subject,template,context)
		return super(Vendor,self).save(*args,**kwargs)
     