from os import path
import json
import yaml
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError

JSON = '.json'
YAML = '.yaml'
YML = '.yml'


def get_data(file_path):
    full_name = path.basename(file_path)
    file_extension = path.splitext(full_name)[-1].lower()

    try:
        with open(file_path, 'r') as file:
            if file_extension == JSON:
                return json.load(file)
            elif file_extension == YAML or file_extension == YML:
                return yaml.load(file, Loader=yaml.FullLoader)
            else:
                raise RuntimeError(f'"{file_extension}" is not supported. '
                                   f'Use json or yaml format')
    except OSError:
        raise RuntimeError(f'"{file_path}" not found')
    except ScannerError:
        raise RuntimeError(f'"{file_path}" is not valid yaml')
    except JSONDecodeError:
        raise RuntimeError(f'"{file_path}" is not valid json')
