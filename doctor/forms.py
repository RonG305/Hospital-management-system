from django import forms
from patient.models import Patient

class patientCreationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'user',  
            'first_name' ,
            'last_name',
            'age' ,
            'weight',
            'height' ,
            'gender',
            'disease',
            'doctor', 
            'blood_group', 
            'approval'
        ]
        
        labels = {
             'user': 'User' ,
            'first_name': 'First name' ,
            'last_name': 'Last name',
            'age': 'age' ,
            'weight': 'weight',
            'height': 'Height' ,
            'gender': 'Gender',
            'disease': 'Disease',
            'doctor': 'Doctor', 
            'blood_group': 'Blood Group', 
            'approval': 'Approval'
        }
        
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}), 
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}) ,
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}) ,
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'disease': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}), 
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'approval': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
