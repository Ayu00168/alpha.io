from django.db import models
from User.models import User

# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name='user')
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True )
    logo = models.ImageField(upload_to='organisation/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisations"
        ordering = ['-created_at']

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()