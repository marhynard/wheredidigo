# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:17:39 2017

@author: matthew.rhynard
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wheredidigo.settings')

import argparse, os, glob
from xml.dom import minidom
import pytz
import datetime

from math import radians, cos, sin, asin, acos, sqrt, pi

import time


import django
from django.db import transaction

django.setup()

from fitparse import FitFile

from fitparser.models import Fileinfo,Point

#TODO figure out a way to distinguish if the activity is a ride or run


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

verbose = False

debug = True

MPSTOMPH = 2.23694


#http://www.johndcook.com/python_longitude_latitude.html
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = pi/180.0
 
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
 
    cos_v = (sin(phi1)*sin(phi2)*cos(theta1 - theta2) + 
           cos(phi1)*cos(phi2))
    arc = acos( cos_v )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc * 6373#6373km 3959mi 

#Michael Dunn StackOverflow 
#    Haversine Formula in Python (Bearing and Distance between two GPS points)
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371000 # Radius of earth in meters. Use 3956 for miles
    return c * r

 
def findDistance(x1, y1,x2,y2):
    c1x = float(x1)
    c1y = float(y1)
    c2x = float(x2)
    c2y = float(y2)
    return haversine(c1x, c1y, c2x, c2y)
	
#def in_list(lat, lon):
#	for point in pointList:
#		if distance(lat,lon,point[1],point[2]) < 40:# distance apart in ft
#			return True
#	return False


#This will give a basic guess as to the activity type.  It is not a guarentee.
#Still need to check and update
#0=unknown, 1=ride, 2=run, 3=swim, 4=other
def getActivityType(speed):
    if speed > 10 and speed < 30:
        return 1
    elif speed > 5 and speed <= 10:
        return 2
    else:
        return 0
    




def read_fit(file_name):
    if debug:
        ti0 = time.clock()
    
    basename = os.path.basename(file_name)
    if Fileinfo.objects.filter(filename=basename).count() == 1:
        print "File exists: ",basename
    else:
        print "File doesn't exist: ",basename
        f = Fileinfo(filename=basename)
        f.save()
        
    fileinfo = Fileinfo.objects.get(filename=basename)

    fitfile = FitFile(file_name)
    average_speed = 0.0
    total_speed = 0.0
    number_records = 0
    with transaction.atomic():
        for record in fitfile.get_messages('record'):
            for record_data in record:
                apoint[record_data.name] = record_data.value
                if apoint[record_data.name] == None:
                    apoint[record_data.name] = 0.0
    
            timeZoneAware = apoint['timestamp'].replace(tzinfo=pytz.UTC)
            if Point.objects.filter(fileid=fileinfo,timestamp=timeZoneAware).count() == 0:
                       
                newPoint = Point(
                    fileid              = fileinfo,
                    altitude            = apoint['altitude'],
                    cadence             = apoint['cadence'],
                    distance            = apoint['distance'],
                    enhanced_altitude   = apoint['enhanced_altitude'],
                    enhanced_speed      = apoint['enhanced_speed'],
                    fractional_cadence  = apoint['fractional_cadence'],
                    position_lat        = apoint['position_lat'],
                    position_long       = apoint['position_long'],
                    speed               = apoint['speed'],
                    timestamp           = timeZoneAware,
                    )
                newPoint.save()
                total_speed += apoint['speed']
                number_records += 1
                average_speed = (total_speed/number_records) * MPSTOMPH
                if verbose:
                    print apoint
                    print average_speed
    
    activity_type = getActivityType(average_speed)    
    fileinfo.activitytype=activity_type
    fileinfo.activityspeed=average_speed
    fileinfo.save()
    
    if verbose:
        print activity_type
    if debug:
        ti1 = time.clock()
        total = ti1-ti0
        print "Time for insert: ",total



def read_tcx(file_name):
    if debug:
        ti0 = time.clock()
    basename = os.path.basename(file_name)
    
    if Fileinfo.objects.filter(filename=basename).count() == 1:
        print "File exists: "
    else:
        print "File doesn't exist: "
        f = Fileinfo(filename=basename)
        f.save()
    
    fileinfo = Fileinfo.objects.get(filename=basename)
    
    xml_node = minidom.parse(file_name)
    
    track = xml_node.getElementsByTagName("Trackpoint")
    counter = 0
    lat1 = 0.0
    lon1 = 0.0
    lat2 = 0.0
    lon2 = 0.0
    t1 = 0
    t2 = 0
    distance = 0.0
    eltime = 0.0
    speed = 0.0
    total_speed = 0.0
    average_speed = 0.0
    number_records = 0.0
    
    
    with transaction.atomic():
        for trackpoint in track:
            time_node       = trackpoint.getElementsByTagName("Time")[0]
            position_node   = trackpoint.getElementsByTagName("Position")
            latitude_node   = position_node[0].getElementsByTagName("LatitudeDegrees")[0]
            longitude_node  = position_node[0].getElementsByTagName("LongitudeDegrees")[0]
            altitude_node   = trackpoint.getElementsByTagName("AltitudeMeters")[0]
            
            date_with_tz    = time_node.childNodes[0].data.strip()
            latitude    = latitude_node.childNodes[0].data.strip()
            longitude   = longitude_node.childNodes[0].data.strip()
            altitude    = altitude_node.childNodes[0].data.strip()
            
            date_str = date_with_tz[:-6]
            dt_utc = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
            pointTime = dt_utc.replace(tzinfo=pytz.UTC)
            
            #timeZoneAware = apoint['timestamp'].replace(tzinfo=pytz.UTC)

    
            if Point.objects.filter(fileid=fileinfo,timestamp=pointTime).count() == 0:
                newPoint = Point(
                    fileid              = fileinfo,
                    altitude            = altitude,
                    position_lat        = float(latitude) * 2147483648 / 180,
                    position_long       = float(longitude) * 2147483648 / 180,
                    timestamp           = pointTime,
                    )
                newPoint.save()
                if counter == 0:
                    lat2 = float(latitude)
                    lon2 = float(longitude)
                    t2 = pointTime
                if counter > 1:
                    lat1 = lat2
                    lon1 = lon2
                    t1 = t2
                    lat2 = float(latitude)
                    lon2 = float(longitude)
                    t2 = pointTime
                    distance = findDistance(lat1, lon1,lat2,lon2)
                    eltime = t2 - t1
                    speed = distance/eltime.total_seconds()
                    total_speed += speed
                    number_records += 1
                    average_speed = (total_speed/number_records) * MPSTOMPH
                
                    
                counter = counter + 1
                
                if verbose:
                    print 'Time,lat,lon,alt: {0}, {1}, {2}, {3}'.format(pointTime,latitude,longitude,altitude)
                    print distance
                    print average_speed
    #        else:
    #            print "Point exists"                
    activity_type = getActivityType(average_speed)    
    fileinfo.activitytype=activity_type
    fileinfo.activityspeed=average_speed
    fileinfo.save()        
    print counter
    if debug:
        ti1 = time.clock()
        total = ti1-ti0
        print "Time for insert: ",total
    
def read_gpx(file_name):
    if debug:
        ti0 = time.clock()    
    basename = os.path.basename(file_name)
    
    if Fileinfo.objects.filter(filename=basename).count() == 1:
        print "File exists: ",basename
    else:
        print "File doesn't exist: ",basename
        f = Fileinfo(filename=basename)
        f.save()
    
    fileinfo = Fileinfo.objects.get(filename=basename)
    
    xml_node = minidom.parse(file_name)

    track = xml_node.getElementsByTagName("trkpt")
    counter = 0
    lat1 = 0.0
    lon1 = 0.0
    lat2 = 0.0
    lon2 = 0.0
    t1 = 0
    t2 = 0
    distance = 0.0
    eltime = 0.0
    speed = 0.0
    total_speed = 0.0
    average_speed = 0.0
    number_records = 0.0
          
    with transaction.atomic():
        for trackpoint in track:
            time_node       = trackpoint.getElementsByTagName("time")[0]
            latitude_node   = trackpoint.getAttribute('lat')
            longitude_node  = trackpoint.getAttribute('lon')
            altitude_node   = trackpoint.getElementsByTagName("ele")[0]
            
            pointTime        = time_node.childNodes[0].data.strip()
            latitude    = latitude_node.strip()
            longitude   = longitude_node.strip()
            altitude    = altitude_node.childNodes[0].data.strip()
            
            if Point.objects.filter(fileid=fileinfo,timestamp=pointTime).count() == 0:
                
                
                newPoint = Point(
                    fileid              = fileinfo,
                    altitude            = altitude,
                    position_lat        = float(latitude) * 2147483648 / 180,
                    position_long       = float(longitude) * 2147483648 / 180,
                    timestamp           = pointTime,
                    )
                newPoint.save()
                if counter == 0:
                    lat2 = float(latitude)
                    lon2 = float(longitude)
                    t2 = time.mktime(datetime.datetime.strptime(pointTime,"%Y-%m-%dT%H:%M:%SZ").timetuple())
                if counter > 1:
                    lat1 = lat2
                    lon1 = lon2
                    t1 = t2
                    lat2 = float(latitude)
                    lon2 = float(longitude)
                    t2 = time.mktime(datetime.datetime.strptime(pointTime,"%Y-%m-%dT%H:%M:%SZ").timetuple())
                    distance = findDistance(lat1, lon1,lat2,lon2)
                    eltime = t2 - t1
                    speed = distance/eltime
                    total_speed += speed
                    number_records += 1
                    average_speed = (total_speed/number_records) * MPSTOMPH
                
                    
                counter = counter + 1
                if verbose:
                    print 'Time,lat,lon,alt: {0}, {1}, {2}, {3}'.format(pointTime,latitude,longitude,altitude)   
                    print distance
                    print average_speed
    #        else:
    #            print "Point exists"
    
    activity_type = getActivityType(average_speed)    
    fileinfo.activitytype=activity_type
    fileinfo.activityspeed=average_speed
    fileinfo.save()        
    print counter
    if debug:
        ti1 = time.clock()
        total = ti1-ti0
        print "Time for insert: ",total

def processFile(filename):
    print "Procssing file: ",filename
    if filename.lower().endswith('.tcx'):
        read_tcx(filename)
    elif filename.lower().endswith('.gpx'):
        read_gpx(filename)
    elif filename.lower().endswith('.fit'):
        read_fit(filename)
    else:
        print "Not a valid format: ",filename
        #fitfile = r'C:\Users\matthew.rhynard\Documents\Python\2096759412.fit'
#    getPointsFromFitFile(r'C:\Users\matthew.rhynard\Documents\Python\2096759412.fit')
#    tcxFile = r'C:\Users\matthew.rhynard\Documents\kmlfiles\Rode 50.27 mi on 04-11-2015.tcx'
#    gpxFile = r'C:\Users\matthew.rhynard\Documents\kmlfiles\activities\20160101-175318-Ride.gpx'
    
    #read_tcx(tcxFile)
#    read_gpx(gpxFile)    
        
    
#files = glob.glob("C:/Users/matthew.rhynard/Documents/kmlfiles/*.tcx")

#for file_name in files:
#	read_tcx(file_name)

#for record in fitfile.get_messages('record'):
#    for record_data in record:
#        if record_data.units:
#            print " * %s: %s %s" % (
#                    record_data.name,record_data.value, record_data.units,
#            )
#        else:
#            print " * %s: %s" % (record_data.name, record_data.value)
#    print

    
    
def main(args):
    global verbose
    
    if args.verbose:
        verbose = args.verbose
    
    if verbose:
        print "Starting to process files..." 

    filename = ''    
    if args.file:
        if verbose:
            print "Processing file: ",args.file
        filename = args.file
        processFile(filename)
    
    else:
        if args.indir:
            if verbose:
                print "Processing Directory: ",args.indir
            if args.filetype:
                if verbose:
                    print "Processing Filetype: ",args.filetype
                files = glob.glob(os.path.join(args.indir,'*'+args.filetype))
                
            else:
                if verbose:
                    print "Processing all filetypes: "
                files = glob.glob(os.path.join(args.indir,'*'))
            
            for filename in files:
                processFile(filename)   
            
        else:
            print "No file or Directory specified"
    
    



    
    
if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--indir'   ,type=str,help="directory which contains the files to be read in")
    arg_parser.add_argument('--filetype',type=str,help='filetypes to process: .tcx,.gpx,.fit')
    arg_parser.add_argument('--file'    ,type=str,help='Process the specified file')
    arg_parser.add_argument('-v','--verbose' ,action="store_true",help='increase output verbosity')
    arg_parser.add_argument('--activity',action="store_true",help='used to try and determine type of activity')
    
    
    args = arg_parser.parse_args()
    
    main(args)
