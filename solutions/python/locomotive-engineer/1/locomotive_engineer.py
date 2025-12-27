"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*arge):
    return list(arge)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first, second, one, *last = each_wagons_id
    *new_wagons, = one, *missing_wagons, *last, first, second
    
    return new_wagons

def add_missing_stops(full_process,**stops_dict):
    *stops, = stops_dict.values()
    full_process["stops"] = stops    
    
    return full_process

def extend_route_information(route, more_route_information):
    new_dict = {**route, **more_route_information}

    return new_dict

def fix_wagon_depot(wagons_rows):
    a, b, c = zip(*wagons_rows)
    a, b, c = list(a), list(b), list(c)
    
    return [a,b,c]