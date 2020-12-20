from gendiff.cli import arg_parse
from gendiff.gendiff import generate_diff


def main():
    args = arg_parse()
    try:
        result = generate_diff(args.first_file,
                               args.second_file,
                               args.format)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
