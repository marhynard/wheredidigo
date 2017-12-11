# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:20:21 2017

@author: matthew.rhynard
"""

from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

from . import views

urlpatterns = [
        #url(r'^$', views.index, name='index'),
		#url(r'^$', views.indexView.as_view()),
		url(r'^$', serve,kwargs={'path': 'index.html'}),
		url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),
        #url(r'^helloworld$', views.HelloWorldPageView.as_view(), name='helloworld'),
        url(r'^helloworld$', views.helloworld, name='helloworld'),
        #url(r'^angulartest$', views.angulartest, name='angulartest'),
        url(r'^manage$', views.getFileList, name='manage'),
        url(r'^pointviewer$', views.pointViewer, name='pointviewer'),
        url(r'^angulartest$', views.HomePageView.as_view()),
        url(r'^links/$' , views.LinksPageView.as_view()),
        url(r'^getcust/$',views.Customers.getCust),

]