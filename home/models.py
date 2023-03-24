from django.db import models

# Create your models here.
class Payment_details(models.Model):
    
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    Services_from_user = models.CharField(max_length=100, blank=True, null=True)
    Services_from_us = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField()