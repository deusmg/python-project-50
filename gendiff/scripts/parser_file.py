#!/usr/bin/env python3

from pathlib import Path
import yaml
import json


def get_data(path):
    with open(path, "r") as data:
        return parse(data.read(), Path(path).suffix[1:])


def parse(data, format: str):
    if format == 'json':
        return json.loads(data)
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(data)
    raise Exception(f"No such method for format: {format}")
