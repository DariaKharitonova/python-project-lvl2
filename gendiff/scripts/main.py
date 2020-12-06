import argparse
import json
from gendiff.get_data.get_data import get_data
from gendiff.gendiff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import get_json_format
from gendiff.formatters.plain import plain


def main():
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

    file1 = get_data(first_file)
    file2 = get_data(second_file)

    result = generate_diff(file1, file2)

    if format == 'stylish':
        print(stylish(result))
    elif format == 'json':
        print(json.dumps(get_json_format(result), indent=2))
    elif format == 'plain':
        print(plain(result))
    else:
        print("Wrong format")


if __name__ == '__main__':
    main()
