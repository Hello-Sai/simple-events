from datetime import datetime
from .models import Event,Registration,Participant
from rest_framework import serializers


'''These are my serializers used for serializing and deserializing data'''
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
class RegistrationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.IntegerField()
    participant = ParticipantSerializer()

    # Validating the Data
    def validate(self, validated_data):
        try:
            '''Validating Whether given event id is correct or incorrect.'''

            event = Event.objects.get(id = validated_data.get('event_id'))
        except Event.DoesNotExist:
            raise serializers.ValidationError('Invalid Event Id. Please Check the  Event Id ')
        except Exception as e:
            raise serializers.ValidationError(e)
        
        '''According to the given assignment One Event object only has to link a participant.'''

        if hasattr(event,'registration'):
            raise serializers.ValidationError('This Event is already registered by a participant.')
        current_date = datetime.now().date()
        if event.date < current_date:
            raise serializers.ValidationError("Event Date has passed")
        return validated_data
    def create(self, validated_data):
        event = Event.objects.get(id = validated_data.pop('event_id'))
        participant = ParticipantSerializer(data=validated_data.pop('participant'))

        ''' Validating Participants 
            Each Participant should have unique email address .'''
        if participant.is_valid(raise_exception=True):
            participant.save()
        return Registration.objects.create(event = event,participant = participant.instance)
    class Meta:
        model = Registration
        fields = '__all__'
        depth = 1