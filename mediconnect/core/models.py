from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_donor = models.BooleanField(default=False)

class BloodDonor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

class MedicineDonor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_made')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='requests_received')
    request_type = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')


