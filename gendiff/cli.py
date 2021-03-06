import argparse
from gendiff.formatters.format_diff import DEFAULT_STYLE, FORMATS


def arg_parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        choices=FORMATS.keys(),
                        default=DEFAULT_STYLE)
    return parser
