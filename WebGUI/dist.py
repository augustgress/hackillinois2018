from math import sin, cos, sqrt, atan2, radians

#lat1 lon1 - initial location, lat2 lon2 - destination
def distApart(lat1, lat2, lon1, lon2):
# approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    return distance

#print(distApart(52.2296,52.406,21.0122,16.925))