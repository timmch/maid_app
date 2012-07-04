from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


allergies_choices = (
	('Cat', 'Cat'),
	('Dog', 'Dog'),
	('Other', 'Other'),
	('None', 'None'),
)
class Employee(models.Model):
	account = models.OneToOneField(User, null=True, blank=True, default = None)
	street_add = models.CharField(max_length=50)
	apt_add = models.CharField(max_length=30, blank=True)
	city_add = models.CharField(max_length=30)
	state_add = models.CharField(max_length=30)
	zip_add = models.IntegerField(null=True, blank=True)
	phone = models.IntegerField(null=True, blank=True)
	dob = models.DateField(null=True, blank=True)
	allergens = models.CharField(max_length=30, choices=allergies_choices, blank=True)
	description = models.TextField(blank=True)
	def get_absolute_url(self):
		return ('view_Employee', None, {'username': self.account.username})
	def __unicode__(self):
		return self.account.username

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			profile = Employee()
			profile.user = instance
			profile.save()

	post_save.connect(create_user_profile, sender=User, dispatch_uid="users-profilecreation-Employee")	

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
