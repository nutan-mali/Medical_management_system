from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100) # The name of the medicine
    description = models.TextField(blank=True, null=True) # Description of the medicine

class Schedule(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  # The medicine associated with this schedule
    # Repetitiveness of the medicine schedule, with choices for daily, weekly, or monthly. 
    repetitiveness = models.CharField(max_length=10, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')])
    # Number of times the medicine should be taken based on the repetitiveness.
    repetition_count = models.IntegerField()

class User(models.Model):
   username = models.CharField(max_length=255, unique=True)
  # Add medical_history field (optional) - Text field or a related model


# This model stores the medical history of a user.
# class UserMedicalHistory(models.Model):
#     # The user associated with this medical history, using a OneToOne relationship.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Medical history information, optional and can be left blank.
#     medical_history = models.TextField(blank=True, null=True)