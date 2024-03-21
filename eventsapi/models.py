from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Participant(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    def __str__(self) -> str:
        return f'{self.name}'

class Registration(models.Model):
    event = models.OneToOneField(Event,on_delete=models.CASCADE)
    participant = models.OneToOneField(Participant,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.event} {self.participant}'