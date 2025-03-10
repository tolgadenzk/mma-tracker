from django.db import models
from django.utils.timezone import now

class TrainingSession(models.Model):
    TRAINING_TYPES = [
        ('Boxing', 'Boxing'),
        ('Kickboxing', 'Kickboxing'),
        ('BJJ', 'Brazilian Jiu-Jitsu'),
        ('Wrestling', 'Wrestling'),
        ('Muay Thai', 'Muay Thai'),
        ('MMA', 'Mixed Martial Arts'),
        ('Conditioning', 'Strength & Conditioning'),
    ]

    title = models.CharField(max_length=200)
    training_type = models.CharField(max_length=50, choices=TRAINING_TYPES)
    duration = models.IntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} - {self.training_type} ({self.duration} min)"

# Create your models here.
