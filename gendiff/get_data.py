import json
import yaml


def get_data(path_to_file):
    my_file = open(path_to_file)
    if path_to_file[-4:] == 'json':
        result_json = json.load(my_file)
        return result_json
    if path_to_file[-4:] == 'yaml' or path_to_file[-3:] == 'yml':
        result_yaml = yaml.safe_load(my_file)
        return result_yaml
