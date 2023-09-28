def diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    added = dict2.keys() - dict1.keys()
    removed = dict1.keys() - dict2.keys()
    result = {}
    for key in keys:
        description = {'key': key}
        if key in removed:
            description['operation'] = 'removed'
            description['value'] = dict1[key]
        elif key in added:
            description['operation'] = 'added'
            description['value'] = dict2[key]
        elif dict1[key] == dict2[key]:
            description['operation'] = 'unchanged'
            description['value'] = dict1[key]
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            description['operation'] = 'nested'
            description['value'] = diff(dict1[key], dict2[key])
        else:
            description['operation'] = 'changed'
            description['old'] = dict1[key]
            description['new'] = dict2[key]
        result[key] = description
    return result