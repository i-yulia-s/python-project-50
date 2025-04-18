import json
from argparse import ArgumentParser

from gendiff.compare import compare_flat


def main():
    desc = 'A utility that finds difference between two configuration files.'
    parser = ArgumentParser(description=desc)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    content1 = json.load(open(args.first_file))
    content2 = json.load(open(args.second_file))
    return compare_flat(content1, content2)


if __name__ == "__main__":
    main()
