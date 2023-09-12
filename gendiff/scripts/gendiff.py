#!/usr/bin/env python3

import argparse
from gendiff import generate_diff
text_disc = 'Compares two configuration files and shows a difference.'
tex = 'set format of output'


def main():
    parser = argparse.ArgumentParser(description=text_disc)
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', type=str, default='stylish', help=tex)

    args = parser.parse_args()

    file_path1 = args.first_file
    file_path2 = args.second_file

    diff = generate_diff(file_path1, file_path2)
    print(diff)


if __name__ == "__main__":
    main()
