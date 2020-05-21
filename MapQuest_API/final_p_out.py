################################
#final_p_out.py output for mapquest information
#
#author:Brian Porter
#
#
#05/11/2018 BP initial version
################################

import final_p_maps


class elevation:
    def output(self,json_output):
        print()
        print("Elavation:")
        lat_long_list = lat_long(json_output)
        for obj in range(o,len(lat_long_list,2)):
                lat_long_single = str(lat_long_list[obj]) + "," + str(lat_long_list[obj + 1])
                json_file = final_p_maps.to_python_obj(final_p_maps.get_elevation(lat_long_single))
                for obj1 in json_file["elevationProfile"]:
                    print((round(obj1["height"])))
class distance:
    def output(self,json_output):
        Print("Distance:",round(json_output["route"]["distance"]),"miles")
class directions:
    def output(self,json_output):
        print("Directions:")
        for obj in json_output["route"]["legs"]:
            for item in (obj["maneuvers"]):
                print(item['narrative'])
        print()
class time:
    def output(self,json_output):
        data = json_output["route"]["time"] / 60
        print("Total Time:",round(data),"minutes")
        print()
class lat_and_long:
    def output(self,json_output):
        data = json_output["route"]["locations"]
        print("LATLONGS")
        for obj in data:
            lat = (obj["displayLatLng"]["lat"])
            lng = ((obj["displayLatLng"]["lng"]))
            if lat > 0:
                direction_lat = "N"
            else:
                diretion_lat = "S"
            if lng > 0:
                direction_lng = "E"
            else:
                direction_lng = "W"
            print('{0:.2f}'.format(abs(lat)) + direction_lat + " " + '{0:.2f}'.format(abs(lng)) + direction_lng)
        print()
    def lat_long(json_output: dict)-> list:
       data = json_output["route"]["locations"]
       lat_long_list = []
       for obj in data:
            lat_long_list.append(obj["displayLatLng"]["lat"])
            lat_long_list.append((obj["displayLatLng"]["lng"]))
       return lat_long_list
    def sort_output(input_list: list)-> list:
        sorted_list = []
        for obj in input_list:
             if obj == "LATLONG":
                 sorted_list.append(lat_and_long())
             elif obj == "STEPS":
                sorted_list.append(narrative_directions())
             elif obj == "TOTALTIME":
                 sorted_list.append(total_time())
             elif obj == "TOTALDISTANCE":
                 sorted_list.append(total_distance())
             elif obj == "ELEVATION":
                 sorted_list.append(elevation())
        return sorted_list
    def start(json_obj: dict, input_list: list):
        for obj in input_list:
            data = obj.output(json_obj)
        return json_obj

