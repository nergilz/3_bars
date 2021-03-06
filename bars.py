import sys
import json
from json.decoder import JSONDecodeError
from math import sqrt


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        list_data_bars = json.load(file_handler)
    return list_data_bars['features']


def get_biggest_bar(list_data_bars):
    biggest_bar = max(
        list_data_bars,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
        )
    return biggest_bar


def get_smallest_bar(list_data_bars):
    smallest_bar = min(
        list_data_bars,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
        )
    return smallest_bar


def get_distance(gps_user, gps_bar):
    return float(sqrt
        (((gps_user[0]-gps_bar[0])**2)+((gps_user[1]-gps_bar[1])**2))
        )


def get_closest_bar(list_data_bars, gps_coordinates):
    closest_bar = min(
        list_data_bars,
        key=lambda x: get_distance(gps_coordinates, x['geometry']['coordinates'])
        )
    return closest_bar


def get_user_gps():
    try:
        longitube = float(input('Input GPS coordinates longitube: '))
        latitube = float(input('Input GPS coordinates latitube: '))
        return [longitube, latitube]
    except ValueError:
        return None


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


def main(file_path):
    list_data_bars = load_data(file_path)
    gps_coordinates = get_user_gps()
    if gps_coordinates is not None:
        bar_inform = get_closest_bar(list_data_bars, gps_coordinates)
        pprint_information(bar_inform, 'Closest')
        pprint_information(get_biggest_bar(list_data_bars), 'Biggest')
        pprint_information(get_smallest_bar(list_data_bars), 'Smallest')
    else:
        print(' Error: GPS coordinates must be input and float type! \n')


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        main(file_path)
    except IndexError:
        print(' Error: No filename for reading!\n')
    except FileNotFoundError:
        print(' Error: file or path "{0}" not found!\n'.format(file_path))
    except JSONDecodeError:
        print(' Error: this is not json-file!\n')
