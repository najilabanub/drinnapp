from rest_frameworkn import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,AdminSerializer,PatientAssistantSerializer,PatientSerializer,RMASerializer,DoctorSerializer
from .models import User,Admin,Doctor,Patient,PatientAssistant,RMA

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class DoctorViewSet(viewsets.ModelViewSet):
     queryset = Doctor.objects.all()
     serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientAssistantViewSet(viewsets.ModelViewSet):
    queryset = PatientAssistant.objects.all()
    serializer_class = PatientAssistantSerializer

class RMAViewSet(viewsets.ModelViewSet):
    queryset = RMA.objects.all()
    serializer_class = RMASerializer
    

