from django.shortcuts import render, redirect
from patient.models import Patient
from django.contrib.auth import decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from accounts.forms import PatientRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.forms import patientProfileForm
from accounts.models import patientProfile



# Create your views here.
@login_required(login_url='patient_login')
def patient(request):
    patients = Patient.objects.all()
    profile = patientProfile.objects.all()    
    context = {
        'patients': patients,
        'profile': profile
    }
    return render(request, 'patient/d_patient.html', context)





def patient_signup(request):
    form = PatientRegisterForm()
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            messages.success(request, 'Your account has been successfully create')
            return redirect('doctor_login')
    context = {
            'form': form
        }
    
    return render(request, 'patient/signup.html', context)

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('patient')
        else:
            return redirect('patient_login')
    return render(request, 'patient/login.html')



def patient_logout(request):
    logout(request)
    return redirect('patient_login')



# PATIENT PROFILE
@login_required(login_url='patient_login')
def profile(request):
    form = patientProfileForm()
    if request.method == 'POST':
        form = patientProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile = request.user
            profile.save()
            messages.success(request, 'Your Profile has been successfully create')
            return redirect('patient')
        
    context = {
            'form': form
        }
    return render(request, 'patient/profile.html', context)

