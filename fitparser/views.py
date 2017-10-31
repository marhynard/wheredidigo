# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .models import Point


# Create your views here.
def index(request):
    existing_points = Point.objects.all()
    context = {'existing_points':existing_points}
    return render(request,'fitparser/index.html',context)
    #return HttpResponse("Hello, world. You're at the fitparse index.")

def helloworld(request):
    context = {}
    return render(request,'fitparser/HelloWorld.html',context)
    
#class HelloWorldPageView(TemplateView):
#    template_name = "fitparser/HelloWorld.html"