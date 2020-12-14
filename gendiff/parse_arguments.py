import argparse
from gendiff.get_data import get_data


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    format = args.format


    result = generate_diff(first_file, second_file)

    if format == 'stylish':
        print(stylish(result))
    elif format == 'json':
        print(get_json_format(result))
    elif format == 'plain':
        print(plain(result))
    else:
        print("Wrong format")