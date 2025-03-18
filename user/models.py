from django.db import models
from django.contrib.auth import AbstractUser
# Create your models here.
class User(AbstractUser):
    User_Type = (('admin','Admin'),
                 ('doctor','Doctor'),
                 ('rma','RMA'),
                 ('patient_assistant','PatientAssistant'),
                 ('patient','Patient'))

    
