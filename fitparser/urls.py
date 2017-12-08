# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:20:21 2017

@author: matthew.rhynard
"""

from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        #url(r'^helloworld$', views.HelloWorldPageView.as_view(), name='helloworld'),
        url(r'^helloworld$', views.helloworld, name='helloworld'),
        #url(r'^angulartest$', views.angulartest, name='angulartest'),
        url(r'^manage$', views.getFileList, name='manage'),
        url(r'^angulartest$', views.HomePageView.as_view()),
        url(r'^links/$' , views.LinksPageView.as_view()),
        url(r'^getcust/$',views.Customers.getCust),

]