from django.db import models
from django.contrib.auth.models import User

# Create your models here.O

class Offence_Type(models.Model):
    version = models.IntegerField(default=0)
    user = models.IntegerField(default=-1)
    offence_name = models.CharField('Name', max_length=500)
    offense_description = models.CharField('Description', max_length=3000)
    class Meta:
        verbose_name = 'Offence Type'
        verbose_name_plural = 'Offence Types'

    def __unicode__(self):
        return self.offence_name

class Location(models.Model):
    version = models.IntegerField(default=0)
    user = models.IntegerField(default=-1)
    location_name = models.CharField('Name',max_length=500)
    location_description = models.CharField('Description', max_length=3000)
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return self.location_name

class Corrective_Period(models.Model):
    version = models.IntegerField(default=0)
    user = models.IntegerField(default=-1)
    period_name = models.CharField('Period Name (for display - e.g. "2 Days")',max_length=1000)
    hours = models.FloatField('Number Of Hours (for an exact deadline - e.g. 48)')
    class Meta:
        verbose_name = 'Corrective Period'
        verbose_name_plural = 'Corrective Periods'
    
    def __unicode__(self):
        return self.period_name
    
class Sub_Contractor(models.Model):
    version = models.IntegerField(default=0)
    user = models.IntegerField(default=-1)
    name = models.CharField('Name',max_length=1000)
    class Meta:
        verbose_name = 'Sub-Contractor'
        verbose_name_plural = 'Sub-Contractors'
    
    def __unicode__(self):
        return self.name
    
class Site(models.Model):
    version = models.IntegerField(default=0)
    user = models.IntegerField(default=-1)
    name = models.CharField('Name',max_length=1000)
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
    
    def __unicode__(self):
        return self.name
    
class Offence_Entry(models.Model):
    offence_type = models.ForeignKey(Offence_Type)
    location = models.ForeignKey(Location)
    corrective_period = models.ForeignKey(Corrective_Period)
    sub_contractor = models.ForeignKey(Sub_Contractor)
    site = models.ForeignKey(Site)
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
    
    def __unicode__(self):
        return self.offence_type
    