from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('patients/', include('patient.urls')),
    path('doctors/', include('doctor.urls')),
    path('accounts/', include('accounts.urls')),


 ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
