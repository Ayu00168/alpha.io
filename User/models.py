from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from organisation.models import Organisation
from utils.roles import ROLE_CHOICES
# Create your models here.

class UserManager(BaseUserManager):
    def create(self, email, password = None, **kwargs):
        if not email:
            raise ValueError('Email is required')
        email  = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user
        
        
        
    
    def create_superuser(self, email, password = None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        if not kwargs.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')
        if not kwargs.get('is_superuser'):  
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password,**kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    objects = UserManager()
    roles = models.CharField(max_length=255, null=True, blank=True, choices=ROLE_CHOICES)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    
    class Meta:
        ordering = ["-is_active", "first_name"]
        
    def __str__(self):
        return self.email