from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from eventsapi.models import  Registration,Event
from eventsapi.serializers import EventSerializer, RegistrationSerializer
# Create your views here.

'''I have used rest_framework viewset it makes easy in serializing data 
    also easily handles the HTTP requests'''
class EventsViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    
class RegistrationViewset(viewsets.ModelViewSet):
    
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def list(self, request, *args, **kwargs):
        return Response("Register to an event using below form.")
    
'''Here I have used Retrieve API view to retrieve particular event data'''

class DetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer