import os
from pathlib import Path
import json
import csv
import pickle


def get_size(path: Path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dir_path, dir_names, filenames in os.walk(path):
            for file in filenames:
                file_path = os.path.join(dir_path, file)
                total_size += os.path.getsize(file_path)
        return total_size


def dir_walker(path: Path):
    result = []
    for root, dir_names, filenames in os.walk(path):
        for name in dir_names + filenames:
            current_path = os.path.join(root, name)
            is_dir = os.path.isdir(current_path)
            size = get_size(Path(current_path))
            parent = os.path.basename(root)
            result.append({
                'name': name,
                'path': current_path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
            })
    return result


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(data, fw, indent=4)


def save_to_csv(data, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as fw:
        csv_write = csv.DictWriter(fw, fieldnames=['name', 'path', 'type', 'size', 'parent'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(data, fw)


def main():
    path = Path(r'D:\Python projects\Advanced_python_course\HW_8\data')
    data = dir_walker(path)
    save_to_json(data, 'jsonfile.json')
    save_to_csv(data, 'csvfile.csv')
    save_to_pickle(data, 'picklefile.pickle')

if __name__ == '__main__':
    main()
