from django.db import models

# Create your models here.

class Location(models.Model):
    """
    A class to store longitude and latitude information about Survivor 
    ...
    Attributes
    ----------
    latitude : DecimalField
        latitude of location
    longitude : DecimalField
        longitude of location
    """

    latitude = models.DecimalField(max_digits=7, decimal_places=5, verbose_name='Latitude')
    longitude = models.DecimalField(max_digits=8, decimal_places=5, verbose_name='Longitude')

class Survivor(models.Model):
    """
    A class to store information about Survivor
    ...

    Attributes
    ----------
    name : CharField
        name of survivor

    age : PositiveSmallIntegerField
        age of survivor

    gender : CharField
        gender of survivor

    is_infected : BooleanField
        flag to specify whether survivor is infected or not
    
    location : Location
        location of survivor
    """

    name = models.CharField(max_length=200, verbose_name='Name')
    age = models.PositiveSmallIntegerField(verbose_name='Age')
    gender = models.CharField(max_length=20, verbose_name='Gender')
    is_infected = models.BooleanField(default=False, verbose_name='Infected')
    location = models.ForeignKey(Location, default=None, null=True, related_name='survivor', on_delete=models.SET_NULL)

