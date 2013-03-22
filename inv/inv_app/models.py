from django.db import models
from django.forms import ModelForm

# Create your models here.
class Person(models.Model):
    ROLE_CHOICES = (
		('Eng', 'Engineering'),
		('Mrkt', 'Marketing'),
		('Fin/Off', 'Finance / Office'), \
		('Care', 'Care'),
		('Sales', 'Sales'),
		)
    name = models.CharField(blank=True, max_length=100)
    role = models.CharField(max_length=100, default = "", choices = ROLE_CHOICES)

    def __unicode__(self):
        return u'%s' % (self.name)

class Item(models.Model):
    COMPUTER_CHOICES = (
		('Dell Latitude E6500', 'Dell Latitude E6500'), 
		('Dell Latitude E5510', 'Dell Latitude E5510'), 
		('Dell Latitude E5500', 'Dell Latitude E5500'), 
		('Dell Latitude E5510', 'Dell Latitude E5510'), 
		('Dell Latitude E6530', 'Dell Latitude E6530'), 
		('Dell Optiplex 390', 'Dell Optiplex 390'), 
		('Dell Latitutde E6520', 'Dell Latitutde E6520'), 
		('Acer Aspire M3450', 'Acer Aspire M3450'), 
		('Lenovo U550 IdeaPad', 'Lenovo U550 IdeaPad'), 
        ('MacBook Pro 13', 'MacBook Pro 13'), 
        ('MacBook Pro A1286', 'MacBook Pro A1286'),
        )
    OS_CHOICES = (
		('Windows 7', 'Windows 7'),
		('Windows 8', 'Windows 8'), 
		('OSX 10.7', 'OSX 10.7'), 
		('OSX 10.8', 'OSX 10.8'), 
		('Ubuntu 12.04', 'Ubuntu 12.04'), 
		('Ubuntu 12.10', 'Ubuntu 12.10'),
        )
    user_name = models.ForeignKey(Person)
    computer_type = models.CharField(max_length=100, default = "", choices = COMPUTER_CHOICES)
    hostname = models.CharField(blank=True, max_length=100)
    serial  = models.CharField(blank=True, max_length=100)
    os = models.CharField(max_length=100, default = "", choices = OS_CHOICES)
    other = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return u'%s' % (self.user_name)

class Printer(models.Model):
    make = models.CharField(blank=True, max_length=100)
    serial = models.CharField(blank=True, max_length=100)
    ip = models.CharField(blank=True, max_length=100)

class Network(models.Model):
    name = models.CharField(blank=True, max_length=100)
    model = models.CharField(blank=True, max_length=100)
    ip = models.CharField(blank=True, max_length=100)
    serial = models.CharField(blank=True, max_length=100)

class Phone(models.Model):
    PHONE_CHOICES = (
        ('SPA504G', 'SPA504G'),
        ('SPA942', 'SPA942'),
        )
    user_name = models.ForeignKey(Person)
    number = models.CharField(blank=True, max_length=100)
    model = models.CharField(max_length=100, default="", choices = PHONE_CHOICES)
    mac = models.CharField(blank=True, max_length=100)

class Monitor(models.Model):
    MODEL_CHOICES = (
        ('NEC Accusync 24', 'NEC Accusync 24'), 
        ('Samsung B2430 24', 'Samsung B2430 24'), 
        ('Samaung 2492 24', 'Samaung 2492 24'), 
        ('Dell 30', 'Dell 30'), 
        ('Samsung T240HD', 'Samsung T240HD'),
        )
    user_name = models.ForeignKey(Person)
    model = models.CharField(max_length=100, default="", choices = MODEL_CHOICES)
    serial = models.CharField(blank=True, max_length=100)
    added_by = models.CharField(blank=True, max_length=100)

class PersonForm(ModelForm):
    class Meta:
        model = Person

class ItemForm(ModelForm):
    class Meta:
        model = Item

class PrinterForm(ModelForm):
    class Meta:
        model = Printer

class NetworkForm(ModelForm):
    class Meta:
        model = Network

class PhoneForm(ModelForm):
    class Meta:
        model = Phone

class MonitorForm(ModelForm):
    class Meta:
        model = Monitor