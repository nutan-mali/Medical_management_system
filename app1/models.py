from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_history = models.TextField(blank=True, null=True)
    

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='medicines',blank=True, null=True)
    def __str__(self):
        return self.name 
    
    
class Schedule(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  # The medicine associated with this schedule
    # Repetitiveness of the medicine schedule, with choices for daily, weekly, or monthly. 
    repetitiveness = models.CharField(max_length=10, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')])
    # Number of times the medicine should be taken based on the repetitiveness.
    repetition_count = models.IntegerField()

    def __str__(self):
        return self.medicine.name

