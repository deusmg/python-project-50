from os.path import splitext
import yaml
import json


def get_data(path):
    _, ext = splitext(path)
    with open(path, "r") as data:
        return parse(data.read(), ext)


def parse(data, format: str):
    if format == '.json':
        return json.loads(data)
    if format == '.yaml' or format == '.yml':
        return yaml.safe_load(data)
    raise Exception(f"No such method for format: {format}")
