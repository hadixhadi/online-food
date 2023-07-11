def detectRole(user):
	if user.role==1:
		redirect_role='VendorDash'
	elif user.role==2:
		redirect_role='CustomerDash'
	elif user.role==None and user.is_admin:
		redirect_role='/admin'
	return redirect_role