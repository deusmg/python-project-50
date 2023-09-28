#!/usr/bin/env python3

import json
import yaml


def parse(file_path):
    file_extension = file_path.split('.')[-1]

    if file_extension in ['yaml', 'yml']:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
    elif file_extension == 'json':
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        raise ValueError("Unsupported file format")

    return data
