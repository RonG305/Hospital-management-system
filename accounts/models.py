from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.

class patientProfile(models.Model):
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    ]
    
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=GENDER)
    locality = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.email
    
    
class DoctorProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=200, null=True, blank=True) 
    department = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.department