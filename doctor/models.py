from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor(models.Model):

    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    department = models.CharField(max_length=250)
    date_registred = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Doctors'
    
    def __str__(self):
        return f"Dr.{self.last_name}"
    
class Patients_attendance(models.Model):
    DAYS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursady', 'Thusday'),
        ('friday', 'Friday')
    ]
    day = models.CharField(max_length=50, choices=DAYS, null=True, blank=True)
    num_patients = models.PositiveIntegerField()
    treated_patients = models.PositiveIntegerField()
    num_outpatients = models.PositiveIntegerField(default=0)
    num_inpatients = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.day