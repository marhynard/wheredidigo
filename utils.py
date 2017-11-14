# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:04:17 2017

@author: matthew.rhynard
"""

from math import radians, cos, sin, asin, acos, sqrt, pi,atan2,degrees


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
def haversine(pointA, pointB):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = pointA[0]
    lon1 = pointA[1]

    lat2 = pointB[0]
    lon2 = pointB[1]
    
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371000 # Radius of earth in meters. Use 3956 for miles
    return c * r

#Comes from the same post as haversine but added by Oleksiy Muzalyev
def initial_bearing(pointA, pointB):

    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = radians(pointA[0])
    lat2 = radians(pointB[0])

    diffLong = radians(pointB[1] - pointA[1])

    x = sin(diffLong) * cos(lat2)
    y = cos(lat1) * sin(lat2) - (sin(lat1)
            * cos(lat2) * cos(diffLong))

    initial_bearing = atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

 
def findDistance(x1, y1,x2,y2):
    c1x = float(x1)
    c1y = float(y1)
    c2x = float(x2)
    c2y = float(y2)
    return haversine((c1x, c1y), (c2x, c2y))