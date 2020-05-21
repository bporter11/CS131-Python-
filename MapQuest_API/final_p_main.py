#############################
#final_p_main.py final project main function/module
#
#
#author:Brian Porter
#
#
#05/12/2018 BP initial version
#############################

import final_p_maps
import final_p_out
def trip_locations():
    number_input = int(input())
    if number_input < 2:
        print("ERROR")
        return trip_locations()
    location_list = []
    for obj in range(number_input):
        location_list.append(input())
    return location_list
def action_outputs():
    number_input = int(input())
    if number_input > 5:
        print("ERROR")
        return action_outputs()
    output_list = []
    for obj in range(number_input):
        output_list.append(input())
    return output_list
if __name__ == "__main__":
    final_p_out.start(final_p_maps.to_python_obj
            (final_p_maps.search(trip_locations())),
            final_p_out.sort_output(action_outputs()))
    print()

