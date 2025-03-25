from django.db import models
from organisation.models import Organisation

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=100)
    is_ocuppied = models.BooleanField(default=False)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.capacity})"
    
    
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.JSONField()
    status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("completed", "Completed"), ("canceled", "Canceled")], default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)