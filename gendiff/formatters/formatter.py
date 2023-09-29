from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


def apply_format(diff_result, format):
    if format == 'stylish':
        return stylish_format(diff_result)
    if format == 'plain':
        return plain_format(diff_result)
    if format == 'json':
        return json_format(diff_result)
    raise Exception(f"You chose the wrong format!: {format}")
