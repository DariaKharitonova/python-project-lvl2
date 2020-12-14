import json
import yaml


def get_data(file_path):
    file_extension = file_path.split(".")[1]

    with open(file_path, 'r') as file:
        if file_extension == 'json':
            return json.load(file)
        elif file_extension == 'yaml' or file_extension == 'yml':
            return yaml.load(file, Loader=yaml.FullLoader)
