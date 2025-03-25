from django.db import models

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    organisation = models.ForeignKey('organisation.Organisation', on_delete=models.CASCADE, related_name='order')
    user = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.product} ({self.quantity})"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    
    
    
class Tables(models.Model):
    table_number = models.CharField(max_length=255)
    table_capacity = models.PositiveIntegerField()
    table_status = models.CharField(max_length=255)
    orders  = models.ManyToManyField(Order, on_delete=models.CASCADE, related_name='table')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.table_number} ({self.table_capacity})"

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"
        ordering = ['-created_at']
