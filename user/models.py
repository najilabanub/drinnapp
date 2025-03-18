from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,user_type = None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(username=username,email = self.normalize_email(email),user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    User_Type = (('admin','Admin'),
                 ('doctor','Doctor'),
                 ('rma','RMA'),
                 ('patient_assistant','Patient Assistant'),
                 ('patient','Patient'))
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    usertype = models.CharField(max_length=15,choices=User_Type,default='patient')

    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','user_type']
    

    def __str__(self):
        return f"{self.username},({self.usertype})"
    
class Admin(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='admin')
        permission = models.TextField(default='all')

        def __str__(self):
            return self.user.username
        
class Doctor(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor')
     specialization = models.CharField(max_length=250)
     experience_years = models.PositiveIntegerField()

     def __str__(self):
          return self.user.username
     
class Patient(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient')
     date_of_birth = models.DateField()
     medical_history = models.TextField(blank=True,null=True)

     def __str__(self):
          return self.user.username
     
class RMA(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='rma')
     assigned_doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,,blank=True)


     def __str__(self):
          return self.user.username
     



class PatientAssistant(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='patientassistant')
     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='assistants')


     def __str__(self):
          return self.user.username