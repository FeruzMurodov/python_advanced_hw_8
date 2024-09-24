import glob
import json
import os
from pathlib import Path


def union_jsons(path: Path):
    default_path = os.getcwd()
    os.chdir(path)
    json_files = glob.glob('*.json')
    merged_data = []
    for file in json_files:
        with open(file, 'r') as fr:
            data = json.load(fr)
            merged_data += data
    os.chdir(default_path)
    with open('all_employees.json', 'w') as fw:
        json.dump(merged_data, fw, indent=4)


if __name__ == '__main__':
    union_jsons(Path(r'D:\Python projects\Advanced_python_course\HW_8\data\zad_2'))
