#!/usr/bin/env python3

from gendiff.scripts.diff import diff
from gendiff.scripts.parser_file import get_data
from gendiff.formatters.formatter import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1 = get_data(path1)
    data2 = get_data(path2)
    result = diff(data1, data2)
    return apply_format(result, format)
