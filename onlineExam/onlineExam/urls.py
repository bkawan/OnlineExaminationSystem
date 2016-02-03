"""onlineExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^classes/', classes, name='classes'),
    url(r'^faq/', faq, name='faq'),
    url(r'^contactus/', contactus, name='contactus'),
    url(r'^doctor/', doctor, name='doctor'),
    url(r'^engineer/', engineer, name='engineer'),
    url(r'^register/', register, name='register'),
    url(r'^login/',login_view, name='login'),
    url(r'^logout/',logout_view, name='logout'),
    url(r'^dashboard/(?P<id>[0-9]+)/', dashboard, name='dashboard'),
    url(r'^recharge', recharge, name='recharge'),
    url(r'^questionset/(?P<qgroup>\w{0,30})/(?P<qset>[0-9]+)/', questionset, name='questionset'),
    url(r'^checkset/(?P<qgroup>\w{0,30})/(?P<qset>[0-9]+)/', checkset, name='checkset'),
    url(r'^rules/(?P<qgroup>\w{0,30})/(?P<qset>[0-9]+)/', rules, name='rules'),
    #api urls
    url(r'api/questions/(?P<qgroup>\w{0,30})/(?P<qset>[0-9]+)/', api_questions),
]

if settings.DEBUG:
    urlpatterns.append(
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
    )
    urlpatterns.append(
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        })
    )
