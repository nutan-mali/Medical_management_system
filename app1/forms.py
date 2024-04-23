from django import forms
from .models import Medicine, Schedule

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description']
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['repetitiveness', 'repetition_count']