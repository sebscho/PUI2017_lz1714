from __future__ import print_function
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os

# make sure this file takes exactly 3 arguments
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_lz1714.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

# fetch and open the data from MTA using MTA_KEY
apiKey = os.getenv(sys.argv[1])
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
    apiKey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)

content_siri_serv_vehi = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
activity = content_siri_serv_vehi[0]['VehicleActivity']

bus_records = open(sys.argv[3], "w")
bus_records.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(len(activity)):
    vehi_info = activity[i]['MonitoredVehicleJourney']
    vehi_location = vehi_info['VehicleLocation']
    Latitude = vehi_location['Latitude']
    Longitude = vehi_location['Longitude']
    try:
        stop_name = vehi_info['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_status = vehi_info['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except vehi_info['OnwardCalls'] == "":
        stop_name = "N/A"
        stop_status = "N/A"
    bus_records.write(str(Latitude) + "," + str(Longitude) + "," + stop_name + "," + stop_status + "\n")
