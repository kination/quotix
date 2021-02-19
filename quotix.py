

def main(argv=None, apply_config=True):
    """Command-line entry."""
    if argv is None:
        argv = sys.argv

    try:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except AttributeError:
        pass

    try:
        # Do something...
    except KeyboardInterrupt:
        return 0


if __name__ == '__main__':
    sys.exit(main())
