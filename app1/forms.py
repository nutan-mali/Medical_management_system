from django import forms
from .models import Medicine, Schedule

class MedicineForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)  # Hidden field for username

    class Meta:
        model = Medicine
        fields = ['username','name', 'description']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['repetitiveness', 'repetition_count']