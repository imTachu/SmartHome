from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os
import requests

'''Clase para las constructoras'''
class ConstructorCompany(models.Model):
    user = models.OneToOneField(User,null=True)
    nit = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    fixed_phone = models.PositiveIntegerField(validators=[MinValueValidator(0000000), MaxValueValidator(9999999)], null=True)
    fixed_phone_extension = models.PositiveIntegerField(validators=[MinValueValidator(00000), MaxValueValidator(99999)], null=True)
    mobile_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    contact_name = models.CharField(max_length=100)

'''Clase para los inmuebles'''
class Property(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100, null=True)
    fixed_phone = models.CharField(max_length=15, null=True)
    plan = models.CharField(max_length=300, null=True)
    constructor_company = models.ForeignKey(ConstructorCompany, null=True)
    is_secure_mode = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

'''Clase extendida de User, se usa para autenticacion, y relaciona las propiedades que un usuario tiene como propietario o residente'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    mobile_number = models.CharField(max_length=15)
    photo = models.CharField(max_length=200, null=True)
    properties_as_resident = models.ManyToManyField(Property, related_name="properties_as_resident")
    properties_as_owner = models.ManyToManyField(Property, related_name="properties_as_owner")

'''Clase para sensores y actuadores'''
class Sensor(models.Model):
    SENSOR_TYPES_CHOICES = (
    	('0', 'Sensor'),
    	('1', 'Actuador'),
    )
    SENSOR_STATUS_CHOICES = (
        ('1', 'Off'),
        ('2', '25%'),
        ('3', '50%'),
        ('4', '75%'),
        ('5', 'On'),
    )
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=60)
    type = models.CharField(max_length=30, choices=SENSOR_TYPES_CHOICES)
    location_in_plan = models.CharField(max_length=20,null=True)
    is_discrete = models.BooleanField(default=False)
    property = models.ForeignKey(Property,null=True)
    value = models.CharField(max_length=30, choices=SENSOR_STATUS_CHOICES)
    
    def __unicode__(self):
        return self.description

'''Clase para eventos'''
class Event(models.Model):
    EVENT_CHOICES = (
        ('0', 'Disparo de alarma'),
        ('1', 'Activar alarma'),
        ('3', 'Alerta en sensor'),
        ('2', 'Desactivar alarma'),
        ('4', 'Cambio actuador'),
    )
    date = models.DateTimeField('date', auto_now_add=True)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30, choices=EVENT_CHOICES)
    is_critical = models.BooleanField(default=False)
    is_fatal = models.BooleanField(default=False)
    property = models.ForeignKey(Property)
    sensor = models.ForeignKey(Sensor)

'''Clase receiver que se ejecuta cuando se recibe un POST de evento para envio de notificaciones (email y SMS)'''
@receiver(post_save, sender=Event)
def EventNotifier(sender, instance, **kwargs):
    print "entra al event notifier! :D"
    print instance.property.name
    '''Se busca la propiedad en la que ocurrio el evento'''
    property_in_event = Property.objects.get(name=instance.property.name)
    address_to_notify = instance.property.address
    name_to_notify = instance.property.name
    sensor = instance.sensor.description
    mail_constructora =  Property.objects.get(name=instance.property.name).constructor_company.email
    constructora =  Property.objects.get(name=instance.property.name).constructor_company
    '''Se busca los datos de uno de los residentes del inmueble'''
    try:
        mobile_to_notify = property_in_event.properties_as_owner.all()[0].mobile_number
        mail_to_notify = property_in_event.properties_as_owner.all()[0].user.email
        first_name = property_in_event.properties_as_owner.all()[0].user.first_name
        last_name = property_in_event.properties_as_owner.all()[0].user.last_name
        
    except UserProfile.DoesNotExist:
        '''Si el inmueble no tiene residentes registrados, se busca el primer duenho'''
        mobile_to_notify = property_in_event.properties_as_resident.all()[0].mobile_number
        mail_to_notify = property_in_event.properties_as_resident.all()[0].user.email
        first_name = property_in_event.properties_as_resident.all()[0].user.first_name
        last_name = property_in_event.properties_as_resident.all()[0].user.last_name
        
    if instance.is_critical == True and property_in_event.is_secure_mode == True:
        print "entra al evento critico"
        text_content = ''
        html_content = render_to_string('watchapp/email.html', {'address_to_notify':address_to_notify, 'name_to_notify':name_to_notify, 'first_name':first_name, 'last_name':last_name, 'sensor': sensor})
        html_content_constructora = render_to_string('watchapp/email_constructora.html', {'constructora': constructora, 'address_to_notify':address_to_notify, 'name_to_notify':name_to_notify, 'first_name':first_name, 'last_name':last_name, 'sensor': sensor, 'mobile_to_notify':mobile_to_notify, 'mail_to_notify':mail_to_notify})
        msg = EmailMultiAlternatives('Alerta en el inmueble ' + address_to_notify + ' ' + name_to_notify, html_content,'watchapp.latam@gmail.com', [mail_constructora])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        msg_constructora = EmailMultiAlternatives('Alerta en el inmueble ' + address_to_notify + ' ' + name_to_notify, html_content_constructora,'watchapp.latam@gmail.com', [mail_constructora])
        msg_constructora.attach_alternative(html_content_constructora, 'text/html')
        msg_constructora.send()
        
    if instance.is_fatal == True and property_in_event.is_secure_mode == True:
        print "entra al evento fatal"
        text_content = ''
        html_content = render_to_string('watchapp/email.html', {'address_to_notify':address_to_notify, 'name_to_notify':name_to_notify, 'first_name':first_name, 'last_name':last_name, 'sensor': sensor})
        html_content_constructora = render_to_string('watchapp/email_constructora.html', {'constructora': constructora, 'address_to_notify':address_to_notify, 'name_to_notify':name_to_notify, 'first_name':first_name, 'last_name':last_name, 'sensor': sensor, 'mobile_to_notify':mobile_to_notify, 'mail_to_notify':mail_to_notify})
        msg = EmailMultiAlternatives('Alerta en el inmueble ' + address_to_notify + ' ' + name_to_notify, html_content,'watchapp.latam@gmail.com', [mail_to_notify])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        msg_constructora = EmailMultiAlternatives('Alerta en el inmueble ' + address_to_notify + ' ' + name_to_notify, html_content_constructora,'watchapp.latam@gmail.com', [mail_constructora])
        msg_constructora.attach_alternative(html_content_constructora, 'text/html')
        msg_constructora.send()
        requests.post(os.environ['BLOWERIO_URL'] + '/messages', data={'to': mobile_to_notify, 'message': 'ATENCION: Alerta fatal: ' + instance.description + ' del inmueble: ' + instance.property.name + '. Mensaje de: Watchapp'})
