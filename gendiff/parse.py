import json
from argparse import ArgumentParser

import yaml

FORMATS = ['json', 'yaml']


def parse_args(arg_list: list[str] | None):
    if arg_list is not None and len(arg_list) < 2:
        raise ValueError('''Invalid arguments.
The function takes a list of two strings with filepaths.''')
    desc = 'A utility that finds difference between two configuration files.'
    parser = ArgumentParser(description=desc)    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args(arg_list)


def get_format(file):
    try:
        file_format = file[file.rindex('.') + 1::]
    except ValueError:
        raise ValueError(f'''Cannot get file format: {file}
Make sure you've specified correct filename and path.''')
    if file_format == 'yml':
        file_format = 'yaml'
    if file_format not in FORMATS:
        raise ValueError(f'''File format is not supported: {file}
Make sure you've specified correct filename and path.''')
    return file_format


def open_file(file):
    try:
        file_format = get_format(file)
    except ValueError as e:
        print(e)
        exit(1)
    match file_format:
        case 'json':
            try:
                return json.load(open(file))
            except (FileNotFoundError, json.JSONDecodeError):
                print(f'Cannot open {file}')
                exit(1)
        case 'yaml':
            try:
                return yaml.load(open(file), Loader=yaml.Loader)
            except (FileNotFoundError, yaml.YAMLError):
                print(f'Cannot open {file}')
                exit(1)
    