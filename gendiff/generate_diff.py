import json
import difflib


def generate_diff(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    differ = difflib.Differ()
    data1_str = json.dumps(data1, indent=2, sort_keys=True, separators=(',', ': ')).splitlines()
    data2_str = json.dumps(data2, indent=2, sort_keys=True, separators=(',', ': ')).splitlines()
    diff = list(differ.compare(data1_str, data2_str))

    result = []
    for line in diff:
        if line.startswith('- '):
            line = line[2:]
            line = line.replace('"', '')
            result.append(f'-{line}')
        elif line.startswith('+ '):
            line = line[2:]
            line = line.replace('"', '')
            result.append(f'+{line}')
        elif line.startswith('  '):
            line = line[1:]
            line = line.replace('"', '')
            result.append(f'{line}')

    return "\n".join(result)
