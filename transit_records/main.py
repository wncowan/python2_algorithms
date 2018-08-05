def transit_analysis(trip_list):
    trip_list_list = []
    users = {}
    cities = {}

    for trip in trip_list:
        trip_as_list = trip.split(":")
        trip_list_list.append(trip_as_list)
    # print trip_list_list

    for trip in trip_list_list:
        if trip[0] not in users:
            users[trip[0]] = trip[3]
        else:
            users[trip[0]] += trip[3]

    for trip in trip_list_list:
        if trip[1] not in cities:
            cities[trip[1]] = 1
        else:
            cities[trip[1]] += 1

        if trip[2] not in cities:
            cities[trip[2]] = 1
        else:
            cities[trip[2]] += 1

    # print "users", users
    # print "cities", cities

    print users.iteritems()
    max_user = None
    for key,value in users.iteritems():
        # print "key, value", key, value
        if not max_user:
            # print "no max"
            max_user = key
            max_distance = value
            # print "max_user", max_user
            # print "max_distance", max_distance
        elif float(value) > float(max_distance):
            # print "updating max_distance and max_user"
            max_user = key
            max_distance = value
        #     print "max_user", max_user
        #     print "max_distance", max_distance
        # print type(max_distance) == type(value)
    # print "max_user", max_user
    # print "max_distance", max_distance
    max_city = None
    for key,value in cities.iteritems():
        if not max_city:
            max_city = key
            max_hits = value
        elif float(value) > float(max_hits):
            max_city = key
            max_hits = value
    print "max_city", max_city
    print "max_hits", max_hits
    print "max_user", max_user
    print "max_distance", max_distance


trips = [
    "C0FFEE1C:CHI:NY:114",
    "T0FFEE1D:LA:NY:212",
    "S0FFEE1C:CHI:LA:314",
    "C0FFEE1C:NY:CHI:814",
    "P0FFEE1C:CHI:SF:114",
]

transit_analysis(trips)
