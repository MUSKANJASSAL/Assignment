"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from details.api import CarList,VehicleList, URLDetail1,URLDetail2, UserAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/cars_list/$', CarList.as_view(), name='car_list'),
    url(r'^api/vehicles_list/$', VehicleList.as_view(), name='vehicle_list'),
    url(r'^api/cars_list/(?P<id>\d+)/$', URLDetail2.as_view(), name='car_list'),
    url(r'^api/vehicles_list/(?P<id>\d+)/$', URLDetail1.as_view(), name='vehicle_list'),
    url(r'^api-token-auth/', UserAuthentication.as_view(), name='User Authentication'),
]
