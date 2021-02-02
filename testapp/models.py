from django.db import models
from .enum_types import CountryList

class CountryCode(models.Model):
    code = models.CharField(max_length=2,
                            choices=[(code, name) for name, code in CountryList.get_alpha_2_country().items()])

    def __str__(self):
        return self.code

class Location(models.Model):
    country_code = models.ForeignKey(CountryCode,on_delete=models.CASCADE)

    @property
    def groups(self):
        groups = list()
        for charge_point in self.charge_points.all():
            groups += list(charge_point.groups.all())
        return groups

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    

class ChargePoint(models.Model):
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE,
        related_name='charge_points',
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='charge_points',
    )

class User(models.Model):
    name = models.CharField(max_length=255, default="no_name")
    username = models.CharField(max_length=150, default='no_username')
    email = models.EmailField(default='no_email@gmail.com')

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='users',
    )


