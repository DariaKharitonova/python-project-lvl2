import argparse
import json
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    with open(args.first_file, 'r') as file:
        file1 = json.load(file)

    with open(args.second_file, 'r') as file:
        file2 = json.load(file)
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
