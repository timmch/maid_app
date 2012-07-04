from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.forms import ModelForm

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    date_of_birth = models.DateField()

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

User.profile = property(lambda u: u.get_profile() )
