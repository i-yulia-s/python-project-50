from argparse import ArgumentParser, Namespace
import json


def main():
    parser = ArgumentParser(prog='gendiff', \
        description='A utility that finds difference between two configuration files.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    content1 = json.dumps(json.load(open(args.first_file)))
    content2 = json.dumps(json.load(open(args.second_file)))
    print(content1)
    print(content2)


if __name__ == "__main__":
    main()
