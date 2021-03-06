import csv

from models import OrbitPath, NearEarthObject


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.
        self.filename = filename
        self.date_to_path_map = {}
        self.name_to_neo_map = {}

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_num = 0
            for row in csv_reader:
                if line_num == 0:
                    line_num = 1
                    continue
                an_orbit_path = OrbitPath(**row)
                if not self.name_to_neo_map.get(row['name'], None):
                    self.name_to_neo_map[row['name']] = NearEarthObject(**row)

                a_near_earth_obj = self.name_to_neo_map.get(row['name'], None)
                a_near_earth_obj.update_orbits(an_orbit_path)

                if not self.date_to_path_map.get(row['close_approach_date'], None):
                    self.date_to_path_map[row['close_approach_date']] = []

                self.date_to_path_map[row['close_approach_date']].append(
                    a_near_earth_obj)

        return None
