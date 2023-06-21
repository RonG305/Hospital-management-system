from django.urls import path
from patient import views


urlpatterns = [
    path('',views.patient, name='patient'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_profile/', views.profile, name='patient_profile'),
    path('patient_signup/', views.patient_signup, name='patient_signup'),
    path('patient_logout/', views.patient_logout, name='patient_logout')
]