import argparse

from os import listdir
from os.path import isfile, join

def command(argv):
    # argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description=__doc__, prog='')
    # TODO: setup arguments
    """
    - d -> docstring
    - q -> quote
    - i -> in place
    """

    parser.add_argument('-f', '--files', default='', help='Define files to be re-formatted')
    parser.add_argument('-d', '--directories', default='', help='Define directories to be re-formatted')

    args = parser.parse_args(argv[1:])
    file_list = set()
    
    if args.files is not None:
        file_list.update(args.files.split(','))

    if args.directories is not None:
        path = args.directories
        file_list.update([join(path, f) for f in listdir(path) if isfile(join(path, f))])

    print(file_list)
