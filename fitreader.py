# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:17:39 2017

@author: matthew.rhynard
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wheredidigo.settings')

import django
django.setup()

from fitparse import FitFile

from fitparser.models import Point


fitfile = FitFile(r'C:\Users\matthew.rhynard\Documents\Python\2096759412.fit')

apoint = {'altitude'            : 0.0,
          'cadence'             : 0.0,
          'distance'            : 0.0,
          'enhanced_altitude'   : 0.0,
          'enhanced_speed'      : 0.0,
          'fractional_cadence'  : 0.0,
          'position_lat'        : 0,
          'position_long'       : 0,
          'speed'               : 0.0,
          'timestamp'           : -1
        }

def getPoints():
    
    for record in fitfile.get_messages('record'):
        for record_data in record:
            apoint[record_data.name] = record_data.value
        newPoint = Point(
                altitude            = apoint['altitude'],
                cadence             = apoint['cadence'],
                distance            = apoint['distance'],
                enhanced_altitude   = apoint['enhanced_altitude'],
                enhanced_speed      = apoint['enhanced_speed'],
                fractional_cadence  = apoint['fractional_cadence'],
                position_lat        = apoint['position_lat'],
                position_long       = apoint['position_long'],
                speed               = apoint['speed'],
                timestamp           = apoint['timestamp'],
                )
        newPoint.save()
        print apoint
        print
    
def main():
    print "main" 
    getPoints()
    
if __name__ == "__main__":
    main()
#for record in fitfile.get_messages('record'):
#    for record_data in record:
#        if record_data.units:
#            print " * %s: %s %s" % (
#                    record_data.name,record_data.value, record_data.units,
#            )
#        else:
#            print " * %s: %s" % (record_data.name, record_data.value)
#    print