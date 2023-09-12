import json
import difflib


def generate_diff(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        d1 = json.load(file1)
        d2 = json.load(file2)

    differ = difflib.Differ()
    d1_str = json.dumps(d1, indent=2, sort_keys=True, separators=(',', ': '))
    d2_str = json.dumps(d2, indent=2, sort_keys=True, separators=(',', ': '))
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
