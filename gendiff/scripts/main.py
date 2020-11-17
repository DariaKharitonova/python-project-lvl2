import argparse
from gendiff.get_data import get_data


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.parse_args()
    first_file_data = get_data(args.path_to_first_file)
    second_file_data = get_data(args.path_to_second_file)
    result_diff = generate_diff(first_file_data, second_file_data)
    print(result_diff)


if __name__ == '__main__':
    main()
