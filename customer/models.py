from django.db import models
from django.contrib.auth.models import User


class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=150)
    customer_email = models.EmailField(
        max_length=100, unique=True, blank=False)
    customer_number = models.CharField(max_length=15, blank=True)
    customer_address = models.TextField()
    assigned_admin = models.ForeignKey(
        User, on_delete=models.CASCADE)

    class Meta:
        db_table = "customer"
