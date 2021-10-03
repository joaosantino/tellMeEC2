import json
import os
dir_root = os.path.abspath('')


def get_file_data(path: str, file: str) -> dict:
    with open(dir_root + path + file) as jsonfile:
        data = json.load(jsonfile)

    return data
