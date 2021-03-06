# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# TODO figure out how to distinguish the various files(filename may not be good enough, may need to come up with another way also)

# Create your models here.

class Fileinfo(models.Model):
    filename = models.CharField(max_length=75,unique=True)
    activitytype = models.IntegerField(default=0) #0=unknown, 1=ride, 2=run, 3=swim, 4=other
    activityspeed = models.FloatField(default=0.0) #m/s
    

class Point(models.Model):
    fileid              = models.ForeignKey(Fileinfo,on_delete=models.CASCADE) #fileid for the file
    altitude            = models.FloatField(default=0.0) #m
    cadence             = models.FloatField(default=0.0) #rpm
    distance            = models.FloatField(default=0.0) #m
    enhanced_altitude   = models.FloatField(default=0.0) #m
    enhanced_speed      = models.FloatField(default=0.0) #m/s
    fractional_cadence  = models.FloatField(default=0.0) #rpm
    position_lat        = models.IntegerField(default=0) #semicircles
    position_long       = models.IntegerField(default=0) #semicircles
    speed               = models.FloatField(default=0.0) #m/s
    timestamp           = models.DateTimeField()
    
