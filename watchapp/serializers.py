from rest_framework import serializers
from watchapp.models import Event, Property, Sensor

class EventSerializer(serializers.HyperlinkedModelSerializer):
    '''Esta clase carga la lista de sensores y propiedades y demas atributos para GET / POST de un evento'''
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Event
        fields = ('id', 'date', 'description', 'value', 'type', 'is_critical', 'is_fatal', 'property', 'sensor')
