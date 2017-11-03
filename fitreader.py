# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:17:39 2017

@author: matthew.rhynard
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wheredidigo.settings')

import sys, math, re, getopt, os, glob
from xml.dom import minidom
#import simplekml
#import time


import django
django.setup()

from fitparse import FitFile

from fitparser.models import Point




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



#http://www.johndcook.com/python_longitude_latitude.html
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
 
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
 
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
 
    # Compute spherical distance from spherical coordinates.
 
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
 
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc* 3959 * 5280#6373km 3959mi 
 
def distance(x1, y1,x2,y2):
    c1x = float(x1)
    c1y = float(y1)
    c2x = float(x2)
    c2y = float(y2)
    return distance_on_unit_sphere(c1x, c1y, c2x, c2y)
	
#def in_list(lat, lon):
#	for point in pointList:
#		if distance(lat,lon,point[1],point[2]) < 40:# distance apart in ft
#			return True
#	return False






def getPointsFromFitFile(filename):
    
    
    fitfile = FitFile(filename)
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
 
def getPointsFromXMLFile(filename):
    
    
    fitfile = FitFile(filename)
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



def get_track_points(xml_node):
    track = xml_node.getElementsByTagName("Trackpoint")
    counter = 0
    
    pointList = []
    
    for trackpoint in track:
		counter = counter + 1
		time = trackpoint.getElementsByTagName("Time")[0]
		position = trackpoint.getElementsByTagName("Position")
		latitude = position[0].getElementsByTagName("LatitudeDegrees")[0]
		longitude = position[0].getElementsByTagName("LongitudeDegrees")[0]
		altitude = trackpoint.getElementsByTagName("AltitudeMeters")[0]
		#if in_list(latitude.childNodes[0].data.strip(),longitude.childNodes[0].data.strip()) == False:
		pointList.append((time.childNodes[0].data.strip(),latitude.childNodes[0].data.strip(),longitude.childNodes[0].data.strip(),altitude.childNodes[0].data.strip()))
		print 'Time,lat,lon,alt: {0}, {1}, {2}, {3}'.format(time.childNodes[0].data.strip(),latitude.childNodes[0].data.strip(),longitude.childNodes[0].data.strip(),altitude.childNodes[0].data.strip())
    print counter
    print len(pointList)

#print xmldoc.toxml()
def read_tcx(file_name):
    xmldoc = minidom.parse(file_name)
    get_track_points(xmldoc)
    

def get_gpx_track_points(xml_node):
    track = xml_node.getElementsByTagName("trkpt")
    counter = 0
    pointList = []
    for trackpoint in track:
        counter = counter + 1
        time = trackpoint.getElementsByTagName("time")[0]
        latitude = trackpoint.getAttribute('lat')
        longitude = trackpoint.getAttribute('lon')
        altitude = trackpoint.getElementsByTagName("ele")[0]
        #if in_list(latitude.childNodes[0].data.strip(),longitude.childNodes[0].data.strip()) == False:
        pointList.append((time.childNodes[0].data.strip(),latitude.strip(),longitude.strip(),altitude.childNodes[0].data.strip()))
        print 'Time,lat,lon,alt: {0}, {1}, {2}, {3}'.format(time.childNodes[0].data.strip(),latitude.strip(),longitude.strip(),altitude.childNodes[0].data.strip())
    print counter
    print len(pointList)
	
def read_gpx(file_name):
    xmldoc = minidom.parse(file_name)
    get_gpx_track_points(xmldoc)



    
def main():
    print "main" 
    #fitfile = r'C:\Users\matthew.rhynard\Documents\Python\2096759412.fit'
#    getPointsFromFitFile(r'C:\Users\matthew.rhynard\Documents\Python\2096759412.fit')
    tcxFile = r'C:\Users\matthew.rhynard\Documents\kmlfiles\Rode 50.27 mi on 04-11-2015.tcx'
    gpxFile = r'C:\Users\matthew.rhynard\Documents\kmlfiles\activities\20160101-175318-Ride.gpx'
    
    read_tcx(tcxFile)
    #read_gpx(gpxFile)    
        
    
#files = glob.glob("C:/Users/matthew.rhynard/Documents/kmlfiles/*.tcx")

#for file_name in files:
#	read_tcx(file_name)


    
    
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