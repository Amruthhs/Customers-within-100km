import os
from math import radians, degrees, sin, cos, asin, acos, sqrt
import json
from operator import itemgetter


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

    def read_file(self):
        """
        Return records with valid distances.
        """

        data = []
        try:
            with open(self.input_file) as f:
                for line in f:
                    data_line = json.loads(line)
                    distance = self.get_distance(self.hq_latitude, self.hq_longitude, float(
                        data_line['latitude']), float(data_line['longitude']))
                    if distance < self.accepted_distance:
                        data.append(data_line)
        except FileNotFoundError:
            raise FileNotFoundError(self.input_file, "cannot be found")
        return data

    def get_closest_customers(self):
        """
        Sort and output valid distances.
        """

        newlist = sorted(self.read_file(), key=itemgetter('user_id'))
        results = []
        for i in newlist:
            results.append(i['name'])
            print(i['name'])
        return results


if __name__ == "__main__":
    cr = CustomerRecords('customer_list.txt', 100000, 53.339428, -6.257664)
    cr.get_closest_customers()