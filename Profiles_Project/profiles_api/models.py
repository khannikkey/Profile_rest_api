from django.db import models
from django.contrib.auth.model import AbstractBaseUser
from django.contrib.auth.model import PermissionMixin
# Create your models here.

class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Retrive Full Name of User"""
        return self.name

    def get_short_name(self):
        """Retrive Short name of User"""
        return self.name

     def __str__(self):
         """Retrive string representation of Our user"""
         return self.email
