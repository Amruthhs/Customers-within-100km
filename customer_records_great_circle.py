import os
from math import radians, degrees, sin, cos, asin, acos, sqrt
from operator import itemgetter
import readfile_input


class CustomerRecords:
    """
    Reads customer file customer_list.txt. 
    Program returns customers within 100000m sorted user_id in ascending order.
    Great-circle distance formula is used to calculate distance.
    """

    def __init__(self, input_file, accepted_distance, hq_latitude, hq_longitude):

        self.input_file = input_file
        self.accepted_distance = accepted_distance
        self.hq_latitude = hq_latitude
        self.hq_longitude = hq_longitude

    def get_distance(self, lat1, lon1, lat2, lon2):
        """
        Distance measurements between two GPS coordinates, returns distance in meters.
        Below Medium blog used for the distance calculation
        https://medium.com/@petehouston/calculate-distance-of-two-locations-on-earth-using-python-1501b1944d97
        """

        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        return 6378137 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
        )

    def get_closest_customers(self):
        """
        Sort and output valid distances.
        """

        newlist = sorted(readfile_input.read_file(self), key=itemgetter('user_id'))
        results = []
        for i in newlist:
            results.append(i['name'])
            print(i['name'])
        return results
