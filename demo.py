#! /usr/bin/env python3


"A demostration of using the argparse module to process command-line arguments."

import argparse

if __name__ == '__main__':
    # Create a command-line parser object
    # We will specify a `formatter_class` that includes the default values for
    # arguments in the help documentation.
    parser = argparse.ArgumentParser(
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    )

    # This `add_argument` method specifies that this script expects 1 or more
    # file paths as positional arguments
    parser.add_argument(
        'file_path',                # The name we'll use to access this argument
        type = str,                  # The type of the argument
        metavar = 'FILE-PATH',       # The placeholder name in the help menu
        nargs = '+',                 # We expect 1 or more file paths
        help = 'A path to a file.',  # The help menu text
    )

    # Using the `add_argument` method again to create an optional keyword
    # argument for an integer
    parser.add_argument(
        '-n', '--number',     # The flags used to specify this option
        type = int,
        default = 1,          # Specifying a default value
        help = 'An integer.',
    )

    # Adding another optional keyword argument for a floating-point number
    parser.add_argument(
        '-t', '--threshold',
        type = float,
        default = 3.4,
        help = 'A super duper important threshold.',
    )

    # Adding another optional boolean keyword argument
    parser.add_argument(
        '-c', '--i-am-cool',
        default = False,
        action = 'store_true',
        help = 'A boolean option.',
    )

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # What does `args` object "look" like?
    print(
        "The args after being processed by the argparse parser object:\n",
        args)

    # We access the arguments specified on the command line (or the default
    # values if they were not used) by using `args.` syntax.
    #
    # For positional arguments (like the first `add_argument` above), we access
    # the value of the arugment using the name we provided as the first
    # argument ("paths")
    print("Paths:", args.file_path)

    # For keyword arguments (like all the rest of the `add_argument` calls
    # above), we access the value of the argument using the the long form of
    # the keyword flag (removing the first two dashes and replacing any other
    # dashes with underscores)
    print("Number:", args.number)
    print("Threshold:", args.threshold)
    print("I am cool?", args.i_am_cool)
