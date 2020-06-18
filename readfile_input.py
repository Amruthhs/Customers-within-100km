import json

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
