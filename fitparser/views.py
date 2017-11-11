# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.views.generic import TemplateView # Import TemplateView
from django.http import HttpResponse
from django.core import serializers
#import json
from .models import Point,Fileinfo


# Create your views here.
def index(request):
    existing_points = Point.objects.all()
    context = {'existing_points':existing_points}
    return render(request,'fitparser/index.html',context)
    #return HttpResponse("Hello, world. You're at the fitparse index.")

#TODO need to fix and make it a valid request
def getFileList(request):
    existing_files = Fileinfo.objects.all()
    context = {'existing_files':existing_files}
    return render(request,'fitparser/manage.html',context)
    
#TODO get the modified list (not quite sure what this means yet)
def getModifiedPointList(request):
    existing_files = Fileinfo.objects.filter()

#TODO need to fix this up and make it so the request is a valid request also need to add it to the urls and create the html and javascript to handle it
def getPointList(request):
    fileid = 1
    existing_points = Point.objects.filter(fileid=fileid)
    
    for point in existing_points:
        point.position_lat = float(point.position_lat) * 180 / 2147483648;
        point.position_long = float(point.position_long) * 180 / 2147483648;
        #print point.position_lat,point.position_long
    js_data = serializers.serialize('json',existing_points)
    context = {'js_data': js_data}
    
    return render(request,'fitparser/HelloWorld.html',context)
    
#TODO add the ability to get specific tracks out
#TODO filter by date
#TODO filter by location

def helloworld(request):
    #existing_points = Point.objects.values_list('position_long','position_lat')
    existing_points = Point.objects.all()
    #semicircles * ( 180 / 2^31 )
    
    for point in existing_points:
        point.position_lat = float(point.position_lat) * 180 / 2147483648;
        point.position_long = float(point.position_long) * 180 / 2147483648;
        #print point.position_lat,point.position_long
    #js_data = json.dumps(existing_points)
    js_data = serializers.serialize('json',existing_points)
    context = {'js_data': js_data}
    
    return render(request,'fitparser/HelloWorld.html',context)
    
#class HelloWorldPageView(TemplateView):
#    template_name = "fitparser/HelloWorld.html"
    

#def testJson(request):
#    data = {}
#    data['key1'] = 'value1'
#    data['key2'] = 'value2'
#    response = HttpResponse(json.dumps(data),content_type="application/json")
#    print response;
    
