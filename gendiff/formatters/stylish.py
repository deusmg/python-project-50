import itertools
REPLACER = '  '
INDENT = '    '


def value_to_str(value, depth):
    if isinstance(value, dict):
        result = []
        for key, val in value.items():
            space = INDENT * (depth + 1)
            result.append(f"\n{space}{key}: {value_to_str(val, depth + 1)}")
        line = itertools.chain('{', result, '\n', [INDENT * depth, '}'])
        return ''.join(line)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def build_line(data, key, depth, INDENT='  '):
    return f"{'  ' * depth}{INDENT}{key}: {value_to_str(data[key], depth + 1)}"


def format_nested(key, value, depth):
    space = REPLACER * (depth + 1)
    nested_lines = walk(value['value'], depth + 1)
    return f"{space * 2}{key}: {nested_lines}"


def format_changed(key, value, depth):
    space = REPLACER * (depth + 1)
    old_line = build_line(value, 'old', depth, '- ')
    new_line = build_line(value, 'new', depth, '+ ')
    return f"{space}{old_line}\n{space}{new_line}"


def format_removed(key, value, depth):
    space = REPLACER * (depth + 1)
    return f"{space}{build_line(value, 'value', depth, '- ')}"


def format_added(key, value, depth):
    space = REPLACER * (depth + 1)
    return f"{space}{build_line(value, 'value', depth, '+ ')}"


def format_unchanged(key, value, depth):
    space = REPLACER * (depth + 1)
    return f"{space}{build_line(value, 'value', depth)}"


def walk(node, depth=0):
    lines = []
    for value in node.values():
        operation = value['operation']
        formatter = globals().get(f'format_{operation}')
        if formatter:
            lines.append(formatter(value['key'], value, depth))
    result = itertools.chain('{', lines, [INDENT * depth + '}'])
    return "\n".join(result)


def stylish_format(diff_result):
    return walk(diff_result)
