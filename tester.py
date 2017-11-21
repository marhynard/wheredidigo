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

from fitparser.models import Point,Fileinfo
import fitparser.views as parserviews

fitfile = FitFile(r'C:\Users\matthew.rhynard\Documents\Python\2096759412.fit')


def testViews():
    print "testViews"
    parserviews.helloworld(None)


def testPointsDatabase():
    print "testPointsDatabase"
    existing_points = Point.objects.all()
    semicirclesconversion = ( float(180) / float(2147483648) )
    count = 0    
    for point in existing_points:
        count += 1
#        print point.fileid
#        point.position_lat = float(point.position_lat) * semicirclesconversion;
#        point.position_long = float(point.position_long) * semicirclesconversion;
#        print point.position_lat,point.position_long
    print count

def testJoinDatabase():
    print "testPointsDatabase"
    existing_points = Point.objects.select_related('fileid')
    semicirclesconversion = ( float(180) / float(2147483648) )
    count = 0    
    for point in existing_points:
        count += 1
        print point.fileid
        print point.fileid.activitytype
        print point.timestamp
#        point.position_lat = float(point.position_lat) * semicirclesconversion;
#        point.position_long = float(point.position_long) * semicirclesconversion;
#        print point.position_lat,point.position_long
    print count

    
def main():
    print "main" 
    #testViews()
    #testPointsDatabase()
    testJoinDatabase()
    
    
    
    
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