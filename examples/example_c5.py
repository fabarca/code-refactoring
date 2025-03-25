"""
Based on example_c4.py

Cognitive Complexity: 7

Changes:
- Create a simple class that allows to read and process a csv based on defined steps

Notes:
- This is an example only for didactic purposes, with a single use of the class, it is actually over-engineering
- Cognitive load increase because of the new class (even if the class is very simple)
- Cognitive complexity metric didn't change
- Composition:
    - the new class allows to build a csv processor by composition
    - it could be helpful if we need to reuse a complex pipeline in several places, modifying only one step at a time
    - in this example is based on duck typing, it could be more robust if we use python protocols

"""

import os


class CSVProcessor:
    def __init__(self, file_reader, csv_parser, csv_processor):
        self.file_reader = file_reader
        self.csv_parser = csv_parser
        self.csv_processor = csv_processor

    def process_csv(self, file_path, sep, cols_to_process):
        csv_lines = self.file_reader(file_path)
        csv_dict = self.csv_parser(csv_lines, sep)
        processed_csv_dict = self.csv_processor(csv_dict, cols_to_process)
        return processed_csv_dict


def read_csv_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    with open(file_path) as file:
        csv_lines = file.readlines()
    return csv_lines


def parse_csv_lines(csv_lines, sep):
    if len(csv_lines[0].split(sep)) == 0:
        raise ValueError(f"csv_lines is not splittable using sep: '{sep}'")
    csv_dict = {}

    # parse CSV header
    col_names = csv_lines[0].strip("\n").split(sep)
    for col_name in col_names:
        csv_dict[col_name] = []

    # parse CSV rows
    for line in csv_lines[1:]:
        col_num = 0
        line = line.strip("\n")
        if len(line) == 0:
            continue
        for column in line.split(sep):
            col_name = col_names[col_num]
            csv_dict[col_name].append(column)
            col_num += 1
    return csv_dict


def process_csv_dict(csv_dict, cols_to_sum):
    csv_dict = csv_dict.copy()
    csv_dict["total"] = [0] * len(csv_dict[cols_to_sum[0]])
    for col_name in cols_to_sum:
        row_num = 0
        for row_value in csv_dict[col_name]:
            csv_dict["total"][row_num] += float(row_value)
            row_num += 1
    return csv_dict


def main():
    file_path = "./data/input.csv"
    sep = ","
    cols_to_sum = ["col2", "col3", "col4"]

    csv_processor = CSVProcessor(read_csv_file, parse_csv_lines, process_csv_dict)

    csv_dict = csv_processor.process_csv(file_path, sep, cols_to_sum)
    print(csv_dict)


main()
