import csv

def parcalanan_sutunlari_yaz(input_file_path, output_file_path, selected_column_index):
    with open(input_file_path, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=';')
        header = next(reader)
        if selected_column_index >= len(header):
            print(f"Error: selected_column_index {selected_column_index} is out of range.")
            return
        else:
            selected_column_data = [row[selected_column_index] for row in reader]
            split_values = [value.replace('|', ',').replace(',', ':').split(':') for value in selected_column_data]
            with open(output_file_path, 'w', newline='') as output_file:
                writer = csv.writer(output_file, delimiter=',')
                for values in split_values:
                    writer.writerow(values)

import csv
from collections import Counter

def write_duplicate_values(input_file_path, output_file_path, selected_column_index):
    with open(input_file_path, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=';')
        selected_column = [row[selected_column_index] for row in reader]

    counter = Counter(selected_column)
    repeated_values = [value for value, count in counter.items() if count > 1]

    with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Duplicate Value'])  
        writer.writerows([[repeated_value] for repeated_value in repeated_values])
import csv

def select_and_write_columns(input_file_path, output_file_path, selected_column_indices, include_header=True):
    selected_columns_data = []

    with open(input_file_path, 'r') as input_file:
        header_line = input_file.readline().strip().split(';')

        if include_header:
            selected_columns_data.append([header_line[i] for i in selected_column_indices])

        for line in input_file:
            row = line.strip().split(';')

            if all(len(row) > index for index in selected_column_indices):
                selected_columns_data.append([row[index] for index in selected_column_indices])
            else:
                print(f"Warning: Satır {line} sütun sayısı yetersiz. Bu satır ihmal edilecek.")

    with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(selected_columns_data)


import csv

def find_ununique_pairs(input_file_path):
    unique_pairs = set()

    with open(input_file_path, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        header = next(reader, [])

        if len(header) < 3:
            print("Error: The file must have at least two columns.")
            return False

        for row in reader:
            pair = (row[0], row[1],row[2])
            if pair in unique_pairs:
                return pair
            else:
                unique_pairs.add(pair)

    return None

input_file_path = 'new_variant_has_disease.csv'
deneme = "deneme.csv"
colum = 0
with open(input_file_path, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=";")
        selected_column = [row for row in reader]




a = write_duplicate_values(input_file_path,deneme,colum)
print(f"{a}")