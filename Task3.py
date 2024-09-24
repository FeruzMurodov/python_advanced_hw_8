import csv
import json
from pathlib import Path
from pprint import pprint


def json_to_csv(path: Path):
    with open(path, 'r', encoding='utf-8') as fr:
        data = json.load(fr)
        print(data)
    with open(f'{path.stem}.csv', 'w', newline='', encoding='utf-8') as fw:
        csv_write = csv.DictWriter(fw, fieldnames=['name', 'price', 'quantity'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    json_to_csv(Path(r'D:\Python projects\Advanced_python_course\HW_8\data\zad_3\products.json'))
