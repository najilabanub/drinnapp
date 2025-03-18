from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,AdminViewSet,DoctorViewSet,PatientAssistantViewSet,PatientViewSet,RMAViewSet




router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'admin',AdminViewSet)
router.register(r'doctor',DoctorViewSet)
router.register(r'patient',PatientViewSet)
router.register(r'patientassistant',PatientAssistantViewSet)
router.register(r'rma',RMAViewSet)



urlpatterns = [

    path('api/',include(router.urls)),
    
]