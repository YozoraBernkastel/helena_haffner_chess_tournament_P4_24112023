import json


def write_json(file, data) -> None:
    file.write(json.dumps(data, indent=4, ensure_ascii=False))
