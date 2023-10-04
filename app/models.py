from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,First_name,Last_name,password=None):
        if not email:
            raise ValueError('enter a mail.....')
        NE = self.normalize_email(email)
        UO = self.model(email=NE,First_name=First_name,Last_name=Last_name)
        UO.set_password(password)
        UO.save()
        return UO
    
    def create_superuser(self,email,First_name,Last_name,password):
        UO = self.create_user(email,First_name,Last_name,password)
        UO.is_staff=True
        UO.is_superuser=True
        UO.save()

        return UO





class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=100,primary_key=True)
    First_name = models.CharField(max_length=39)
    Last_name = models.CharField(max_length=19)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['First_name','Last_name']
    objects = UserProfileManager()
