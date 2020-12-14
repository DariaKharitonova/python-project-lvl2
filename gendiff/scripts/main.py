import argparse
from gendiff.gendiff import generate_diff


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

    result = generate_diff(first_file, second_file, format)
    print(result)


if __name__ == '__main__':
    main()
