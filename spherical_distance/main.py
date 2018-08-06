from math import *

def travel_distance(trip_list):
    trip_list_list = []
    for info in trip_list:
        info_list = info.split(":")
        trip_list_list.append(info_list)
    print trip_list_list
    psi1 = float(trip_list_list[0][2])
    psi2 = float(trip_list_list[1][2])
    k1 = float(trip_list_list[0][3])
    k2 = float(trip_list_list[1][3])
    print "k1", k1
    print "k2", k2
    print "psi1", psi1
    print "psi2", psi2
    delta_k = abs(float(k1)-float(k2))
    print delta_k
    delta_sigma = acos(( sin(psi1) * sin(psi2) ) + ( cos(psi1) * cos(psi2) * cos(delta_k) ))
    radius_earth = 3959 
    distance = radius_earth * delta_sigma
    print distance
 
CHI = "LOC:CHI:41.836944:-87.684722"
NYC = "LOC:NYC:40.7127:-74.0059"
TRIP = "TRIP:C0FFEE1C:CHI:NYC"

a_trip_list = [CHI, NYC, TRIP]
travel_distance(a_trip_list)
