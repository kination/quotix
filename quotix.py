import os
import signal
import sys

from src.command import command

def main(argv=None, apply_config=True):
    """Command-line entry."""
    if argv is None:
        argv = sys.argv

    try:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except AttributeError:
        pass

    try:
        return command(argv)
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    sys.exit(main())
