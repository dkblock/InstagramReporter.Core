import json


def pretty(dictionary):
    return json.dumps(
        dictionary,
        indent=4,
        separators=(',', ': '),
        ensure_ascii=False,
    )
