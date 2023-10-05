#!/usr/bin/env python
from gendiff import generate_diff
from gendiff.cli import parser_args


def main():
    args = parser_args()
    print(generate_diff(args.first_file, args.second_file, format=args.format))


if __name__ == '__main__':
    main()
