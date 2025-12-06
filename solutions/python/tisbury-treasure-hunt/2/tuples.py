"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    # record: tuple - with a (treasure, coordinate) 

    return record[1]

def convert_coordinate(coordinate):
    # coordinate: str - a string map coordinate
    new_coordinate = tuple(coordinate) # new coordinate (新座標)

    return new_coordinate

def compare_records(azara_record, rui_record):
    # azara_record: tuple - (treasure, coordinate)
    # rui_record: tuple - (location, tuple(coordinate_1, coordinate_2), quadrant)

    return tuple(azara_record[1]) == rui_record[1]
    
def create_record(azara_record, rui_record):
    # azara_record: tuple - (treasure, coordinate)
    # rui_record: tuple - (location, tuple(coordinate_1, coordinate_2), quadrant)
    
    if compare_records(azara_record, rui_record):
        new_record = azara_record + rui_record
    else:
        new_record = "not a match"

    return new_record


def clean_up(combined_record_group):
   # combined_record_group: tuple - everything from both participants.
    new_record = ""
    
    for i in combined_record_group:
        record = (i[0], i[2], i[3], i[4])
        new_record = new_record + str(record) + "\n"
            

    return new_record    