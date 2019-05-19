#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import sys

if sys.version_info >= (3,):
    import urllib.request as urllib2
else:
    import urllib2


url = 'http://ipinfo.io/json'
response = urllib2.urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
loc = data['loc']

print('Your IP detail :- \n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0} \nloc : {5}'.format(org,region,country,city,IP,loc))

import socket
machine_ip = socket.gethostbyname(socket.gethostname())
print('machine_ip = ',machine_ip)

import folium

import ipinfo

access_token = '476be2099ddd6f'
handler = ipinfo.getHandler(access_token,request_options={'timeout': 4})
def get_ip_details(ip_address):
    details = handler.getDetails(ip_address)
    #print(details.all)
    return details.country_name,details.city,details.org,float(details.latitude),float(details.longitude)

ip_address = '183.87.175.153'
country,city,org,latitude,longitude = get_ip_details(ip_address)
#print(country,city,hostname,latitude )
print('country : {0} \ncity : {1} \nOrg : {2} \nloc : {3} {4}\n'.format(country,city,org,latitude,longitude))

ip_loc = (latitude,longitude)
print("ip_loc = ",ip_loc)

def generate_map_from_loc(latitude,longitude,org):
    map_osm = folium.Map(location=[latitude,longitude],zoom_start=13,tiles='openstreetmap')
    folium.TileLayer('openstreetmap').add_to(map_osm)
    folium.Marker(location=[latitude,longitude],popup=org,icon=folium.Icon(color='red',icon_color='black',icon='info-sign',angle=0),tooltip=org).add_to(map_osm)
    folium.LayerControl().add_to(map_osm)
    map_osm.save('C:/Users/khushal/Documents/Python Scripts/Proxy_loc.html')

generate_map_from_loc(latitude,longitude,org)