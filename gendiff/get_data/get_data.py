import json
import yaml

JSON = 'json'
YAML = 'yaml'


def get_data(file_path):
    file_extension = file_path.split(".")[1]

    with open(file_path, 'r') as file:
        if file_extension == JSON:
            return json.load(file)
        elif file_extension == YAML:
            return yaml.load(file, Loader=yaml.FullLoader)
