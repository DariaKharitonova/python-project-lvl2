import argparse
from gendiff.formatters.formater import DEFAULT_STYLE, VIEW_STYLES


def arg_parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        choices=VIEW_STYLES.keys(),
                        default=DEFAULT_STYLE)
    return parser.parse_args()
