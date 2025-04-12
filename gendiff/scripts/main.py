from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog='gendiff', \
        description='A utility that finds difference between two configuration files.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.parse_args()
    print("Hello from python-project-50!")


if __name__ == "__main__":
    main()
