from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from doctor.models import Doctor
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    BLOOD_GROUPS = [
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
    ]
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    ]

    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    patient_id = models.AutoField(auto_created=True, null=False, primary_key=True, )
    first_name = models.CharField(max_length=250, blank=True, null=False)
    last_name = models.CharField(max_length=250, blank=True, null=False)
    age = models.IntegerField(default=1, validators = [MaxValueValidator(160), MinValueValidator(1)])
    weight = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=8)
    height = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=4)
    gender = models.CharField(max_length=20, choices=GENDER )
    disease = models.CharField(max_length=100, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    blood_group = models.CharField(max_length=50, choices=BLOOD_GROUPS)
    approval = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Appointment(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    image = models.ImageField()
    consultant = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    appointment_type = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank= True)
        
    class Meta:
        verbose_name_plural = 'appointments'
             
    def __str__(self):
        return f'{self.consultant}'  
         
            
       
        