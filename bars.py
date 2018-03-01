import sys
import json
from json.decoder import JSONDecodeError
from math import sqrt


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        json_content = json.load(file_handler)
    return json_content['features']


def get_biggest_bar(json_content):
    biggest_bar = max(
        json_content,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(json_content):
    smallest_bar = min(
        json_content,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def distance_calculation(gps_user, gps_bar):
    return float(sqrt
        (((gps_user[0]-gps_bar[0])**2)+((gps_user[1]-gps_bar[1])**2))
        )


def get_closest_bar(json_content, gps_coordinates):
    closest_bar = min(
        json_content,
        key=lambda x: distance_calculation(
            gps_coordinates,
            x['geometry']['coordinates']
            )
        )
    return closest_bar


def input_gps():
    try:
        longitube = float(input('Input GPS coordinates longitube: '))
        latitube = float(input('Input GPS coordinates latitube: '))
        return [longitube, latitube]
    except ValueError:
        print(' Error: GPS coordinates must be input and float type! \n')
        sys.exit()


def pprint_information(bar_inform, pointer):
    print(
        '\n{0} bar name : {1}\n'
        '{0} bar address : {2}\n'
        '{0} bar phone : {3}\n'.format(
            pointer,
            bar_inform['properties']['Attributes']['Name'],
            bar_inform['properties']['Attributes']['Address'],
            bar_inform['properties']['Attributes']['PublicPhone'][0]['PublicPhone'],
            )
        )


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        json_content = load_data(file_path)
        gps_coordinates = input_gps()
        pprint_information(get_biggest_bar(json_content), 'Biggest')
        pprint_information(get_smallest_bar(json_content), 'Smallest')
        pprint_information(get_closest_bar(json_content, gps_coordinates), 'Closest')
    except IndexError:
        print(' Error: No filename for reading!\n')
    except FileNotFoundError:
        print(' Error: file or path "{0}" not found!\n'.format(file_path))
    except JSONDecodeError:
        print(' Error: this is not json-file!\n')
