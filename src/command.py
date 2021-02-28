import argparse

def command(argv):
    
    # argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description=__doc__, prog='')
    # TODO: setup arguments
    args = parser.parse_args(argv[1:])


