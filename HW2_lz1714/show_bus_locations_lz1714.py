'''Input: This python script takes in the API key and the bus line number.
   Output: bus line number, number of active buses, each bus's latitude and longitude.'''
from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# make sure this file takes exactly 2 arguments
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_lz1714.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# fetch and open the data from MTA through the SIRI API.
# set the API KEY to an environment variable so that other people can use their
# own key and the same environment varialble name to read the data.
apiKey = os.getenv(sys.argv[1])
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apiKey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)

# locate vehicle information
content_siri_serv_vehi = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
activity = content_siri_serv_vehi[0]['VehicleActivity']

# output 
print ("Bus Line :", sys.argv[2])
print ("Number of Active Buses :", len(activity))
for i in range(len(activity)):
    vehi_info = activity[i]['MonitoredVehicleJourney']
    vehi_location = vehi_info['VehicleLocation']
    Latitude = vehi_location['Latitude']
    Longitude = vehi_location['Longitude']
    print ("Bus", i, "is at latitude", Latitude, "and longitude", Longitude)
