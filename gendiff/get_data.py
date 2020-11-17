import json
import yaml


def get_data(path_to_file):
    my_file = open(path_to_file)
    if path_to_file[-4:] == 'json':
        result = json.load(my_file)
        return result
    if path_to_file[-3:] == 'yml' or path_to_file[-4:] == 'yaml':
        result = yaml.safe_load(my_file)
        return result
