########################################
#finalout.py Classes for the parsed API results
#
#
#author:Brian Porter
#
#
#BP initial version 05/12/2018
########################################

import final_maps

class Steps:
    def generate(self, json_result:'json')->list:
        return final_maps.parse_steps(json_result)
class Distance:
    def generate(self, json_result:'json')->int:
        return final_maps.parse_distance(json_result)
class Time:
    def generate(self, json_result:'json')->int:
        return final_maps.parse_time(json_result)
class LatLong:
    def generate(self, json_result:'json')->list:
        return final_maps.parse_latlong(json_result)

