from django.urls import path
from doctor import views

urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('patients_data/', views.patients_data, name='patients_data'),
    path('add_patient/', views.create_patient, name= 'add_patient'),
    path('patient_view/<str:patient_id>', views.patient_view, name='patient_view'),
    path('delete_patient/<str:pk>/', views.delete_patient, name='delete_patient'),
    path('update_patient/<str:pk>/', views.update_patient, name='update_patient'),
    path('doctor_signup/', views.doctor_signup, name='doctor_signup'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_logout/', views.doctorLogout, name="doctor_logout")
    
]