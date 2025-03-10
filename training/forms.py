from django import forms
from .models import TrainingSession

class TrainingForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'training_type', 'duration', 'notes']
