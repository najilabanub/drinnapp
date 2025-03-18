from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User,Admin,Doctor,Patient,PatientAssistant,RMA
from rest_framework_simplejwt.tokens import RefreshToken



class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model =  User
        fields = ['id','email','username','usertype']

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['id','user','permission']

class DoctorSerializer(serializers.ModelSerializer):

    user = UserSerializer
    class Meta:
        model = Doctor
        field = ['id','user','specialization','experience_years']


class PatientSerializer(serializers.ModelSerializer):
     user = UserSerializer

     class Meta:
         model = Patient
         fields = ['id','user','date_of_birth','medical_history']


class RMASerializer(serializers.ModelSerializer):
    user =UserSerializer


    class Meta:
        model = RMA
        fields = ['id','user','assigned_doctor']

class PatientAssistantSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = PatientAssistant
        fields = ['id','user','patient']