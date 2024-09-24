import csv
from pathlib import Path


def modify_csv(path: Path):
    quantities = {}
    with (open(path, 'r', newline='') as fr):
        csv_read = csv.DictReader(fr)
        for row in csv_read:
            temp_dict = dict(row)
            print(temp_dict)
            product, quantity, price = temp_dict['product'], temp_dict['quantity'], temp_dict['price']
            if product in quantities.keys():
                quantities[product] += int(quantity)
            else:
                quantities[product] = int(quantity)

        print('---')
        print(quantities)


if __name__ == '__main__':
    modify_csv(Path(r'D:\Python projects\Advanced_python_course\HW_8\data\zad_4\sales.csv'))
