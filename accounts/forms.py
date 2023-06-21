from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import patientProfile, DoctorProfile


class DoctorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        
        
class PatientRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            
        ]  
        
            
class patientProfileForm(forms.ModelForm):
    class Meta:
        model = patientProfile
        fields = [
            
            'image',
            'first_name',
            'last_name',
            'age',
            'email' ,
            'gender',
            'locality' ,
            'mobile' 
        ]  
        
        
        labels = {
            
            'image': 'Profile picture',
            'first_name:': 'First name',
            'last_name': 'Last name',
            'age': 'age',
            'email': 'Email Address' ,
            'gender': 'Gender',
            'locality': 'Locality' ,
            'mobile': 'Mobile number', 
        }   
        
        widgets = {
           
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}) ,
            'gender':  forms.Select(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}), 
        }
        
        
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
           
            'image',
            'name',
            'department'
        ]  
        
        labels = {
           
            'image': 'Profile',
            'name': 'Full name',
            'department': 'Department'
        }
        
        widgets = {
         
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'})
        }        
        
          