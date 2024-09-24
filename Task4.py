import csv
from pathlib import Path


def revenue_calc(path: Path):
    rows = []
    with open(path, 'r', newline='', encoding='utf-8') as fr:
        csv_reader = csv.reader(fr, dialect='excel')
        for i, line in enumerate(csv_reader):
            if i != 0:
                rows.append({'product': line[0], 'revenue':(round(int(line[1]) * float(line[2]), 2))})
        print(rows)
    with open('total_sales.csv', 'w', newline='', encoding='utf-8') as fw:
        csv_write = csv.DictWriter(fw, fieldnames=['product', 'revenue'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    revenue_calc(Path(r'D:\Python projects\Advanced_python_course\HW_8\data\zad_4\sales.csv'))
