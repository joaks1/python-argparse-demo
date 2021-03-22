#! /usr/bin/env python3

import argparse

if __name__ == '__main__':

    # Create a command-line parser object
    # We will specify a `formatter_class` that includes the default values for
    # arguments in the help documentation.
    parser = argparse.ArgumentParser(
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    # Let's add positional arguments
    # This `add_argument` specifies that this script expects 1 or more file
    # paths as positional arguments
    parser.add_argument('paths',
            type = str,
            metavar = 'PATH',
            nargs = '+', # 1 or more
            help = 'A path to a file.')
    parser.add_argument('-n', '--number',
            type = int,
            default = 1,
            help = 'An integer. Default: 1')
    parser.add_argument('-t', '--threshold',
            type = float,
            default = 3.4,
            help = 'A super duper important threshold.')
    parser.add_argument('-c', '--i-am-cool',
            default = False,
            action = 'store_true',
            help = 'A boolean option.')

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()
    print(args)
    print("Paths:", args.paths)
    print("Number:", args.number)
    print("Threshold:", args.threshold)
    print("I-am-cool:", args.i_am_cool)
