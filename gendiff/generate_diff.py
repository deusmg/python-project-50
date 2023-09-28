#!/usr/bin/env python3

import difflib
import json
from gendiff.scripts import parser_file


def generate_diff(file1_path, file2_path):
    # Парсинг первого файла
    data1 = parser_file.parse(file1_path)

    # Парсинг второго файла
    data2 = parser_file.parse(file2_path)

    differ = difflib.Differ()
    d1_str = json.dumps(data1, indent=2, sort_keys=True, separators=(',', ': '))
    d2_str = json.dumps(data2, indent=2, sort_keys=True, separators=(',', ': '))
    d1_str = d1_str.splitlines()
    d2_str = d2_str.splitlines()
    diff = list(differ.compare(d1_str, d2_str))

    result = []
    for line in diff:
        if line.startswith('- '):
            line = line[3:]
            line = line.replace('"', '')
            result.append(f' - {line}')
        elif line.startswith('+ '):
            line = line[3:]
            line = line.replace('"', '')
            result.append(f' + {line}')
        elif line.startswith('  '):
            line = line[3:]
            line = line.replace('"', '')
            result.append(f'   {line}')

    return '{' + "\n".join(result) + '}'.rstrip(' ')
