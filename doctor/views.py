from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from patient.models import Appointment, Patient
from hospital.models import Room
from doctor.forms import patientCreationForm
from doctor.models import Patients_attendance


from accounts.forms import DoctorRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def doctor(request):
    labels = []
    data = []

    attendance = Patients_attendance.objects.order_by('-num_patients')[:5]
    for attend in attendance:
        labels.append(attend.day)
        data.append(attend.num_patients)

   
    appointments = Appointment.objects.order_by('date')
    num_appointments = Appointment.objects.all().count()
    num_patients = Patient.objects.all().count()
    num_rooms = Room.objects.all().count
    Patients_attendance = Patients_attendance.objects.all().count()
    

    context = {
       
        'appointments': appointments,
        'num_appointments': num_appointments,
        'num_patients': num_patients,
        'num_rooms': num_rooms,
        'labels': labels,
        'data': data,
        
        
    }
    return render(request, 'doctor/doctor.html', context)


def patient_view(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    context = {
        'patient': patient
    }
    
    return render(request, 'doctor/patient_view.html', context)




def patients_data(request):
    patients = Patient.objects.all()
    
    context = {
        'patients': patients,
    }
    
    return render(request, 'doctor/patients.html', context)


def create_patient(request):
    form = patientCreationForm()
    if request.method == 'POST':
        form = patientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_data')      
  
    context = {
        'form': form
    }
    return render(request, 'doctor/add_patient.html', context)

def update_patient(request, pk):
    
    patient = Patient.objects.get(pk=pk)
    form = patientCreationForm(instance=patient)
    
    if request.method == 'POST':
        form = patientCreationForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients_data')
        
    context = {
        'form': form
        }
    return render(request, 'doctor/patient_update.html', context)   



def delete_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.delete()
    

def doctor_signup(request):
    form = DoctorRegisterForm()
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            messages.success(request, 'Your account has been successfully create')
            return redirect('doctor_login')
    context = {
        'form': form
        }
    
    return render(request, 'doctor/signup.html', context)

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('doctor')
    return render(request, 'doctor/login.html')



def doctorLogout(request):
    logout(request)
    return redirect('doctor_login')