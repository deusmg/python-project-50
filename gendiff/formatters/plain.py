def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    return f"'{value}'"


def walk(node, path=''):
    result = []
    for key, val in node.items():
        current_path = f"{path}{val['key']}"
        start_line = f"Property '{current_path}'"
        if val['operation'] == 'changed':
            result.append(f"{start_line} was updated. "
                          f"From {to_str(val['old'])} to {to_str(val['new'])}")
        if val['operation'] == 'nested':
            result.append(walk(val['value'], current_path + '.'))
        if val['operation'] == 'removed':
            result.append(f"{start_line} was removed")
        if val['operation'] == 'added':
            result.append(f"{start_line} was added "
                          f"with value: {to_str(val['value'])}")
    return '\n'.join(result)


def plain_format(diff_result: dict):
    return walk(diff_result)
