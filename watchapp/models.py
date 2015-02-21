from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

'''Clase extendida de User, se usa para autenticacion, '''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    STYLE_CHOICES = (
    	('afternoon', 'afternoon'),
    	('blitzer', 'blitzer'),
    	('dark-hive', 'dark-hive'),
    	('sunny', 'sunny'),
    )
    style = models.CharField(max_length=30, choices=STYLE_CHOICES, default='afternoon')

class Team(models.Model):
	name = models.CharField(max_length=100)
	users = models.ManyToManyField(UserProfile)

class AddressBook(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	team = models.ForeignKey(Team, null=True, unique=False)

class Contact(models.Model):
    given_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    skype = models.CharField(max_length=100, null=True)
    googleplus = models.CharField(max_length=100, null=True)
    address_book = models.ForeignKey(AddressBook)
	
class Localization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact = models.ForeignKey(Contact, null=True)
	
class PhoneNumber(models.Model):
	phone = models.PositiveIntegerField(validators=[MinValueValidator(0000000), MaxValueValidator(9999999999)])
	localization = models.ForeignKey(Localization, null=True)
	
class Address(models.Model):
	address = models.CharField(max_length=100)
	localization = models.ForeignKey(Localization, null=True)

class Email(models.Model):
	email = models.EmailField(max_length=50, blank=False, unique=True)
	localization = models.ForeignKey(Localization, null=True)
	
